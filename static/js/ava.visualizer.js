/**
 * AVA D3 Visualizer
 * @module AVA.Visualizer
 */
/* jshint unused: false, newcap: false */
(function (root, factory) {
   'use strict';
   // UMD Header. https://github.com/umdjs/umd
   if (typeof define === 'function' && define.amd) { var dependencies = []; define(dependencies, factory); }
   else if (typeof exports === 'object') { module.exports = factory(); }
   else {
      if ( typeof root.AVA === 'undefined' ) { root.AVA = {}; }
      root.AVA.Visualizer = factory();
   }
}(this, function(){
   'use strict';

   var configDefaults = {
      'elementId': 'graph',
      'statsElementId': false,
      'dataCallback': false
   };

   function Visualizer(config){

      var module = {};

      function getBounds(){
         return {w: $(window).width(), h: $(window).height()};
      }

      var stats = false;

      var currentData = false;

      var svg = false;
      var force = false;
      var color = d3.scale.category20();
      var nodes = [];
      var links = [];
      var node = false;
      var link = false;
      var drawLines = false;
      var drawLabels = true;

      function tick(){
         if ( stats ) stats.begin();
         var bounds = getBounds();
         var r = 50;
         if ( drawLines ) {
            link.attr("x1", function (d) { return d.source.x; })
               .attr("y1", function (d) { return d.source.y; })
               .attr("x2", function (d) { return d.target.x; })
               .attr("y2", function (d) { return d.target.y; });
         }
         node.attr("transform", function(d){
            /*d.x = Math.max(r, Math.min(bounds.w - r, d.x));
            d.y = Math.max(r, Math.min(bounds.h - r, d.y));*/
            return "translate(" + d.x + "," + d.y + ")";
         });
         if ( stats ) stats.end();
      }

      function endForce(){
         console.log('endForce');
         drawLines = true;
         link.style({"visibility": "visible", 'opacity': 0})
            .transition()
            .duration(250)
            .style('opacity', 1);
         // force one tick
         tick();
      }

      function startForce(){
         console.log('startForce');
         drawLines = false;
         link.style("visibility", "hidden");
      }

      // Lowercases, replaces whitespace with _, strips non a-z0-9
      function stringToDomName(str){
         return str.toLowerCase().replace(/\W+/g, '_').replace(/[^a-z0-9]/g,'');
      }

      function inputChange(inputData){

         _.chain(inputData.nodes)
            .filter({'node_type': 'group'})
            .each(function(groupNode){
               groupNode.nodeId = 'G_' + groupNode.id;
               groupNode.id = stringToDomName(groupNode.cn);
            });

         //TODO: Filter this properly
         force.links(inputData.links);
         force.nodes(inputData.nodes);

         if ( config.dataCallback ) config.dataCallback(inputData.nodes);

         var connectionCounts = {};
         _.each(inputData.links, function(d){
            connectionCounts[d.source] = ( typeof connectionCounts[d.source] === 'undefined' ? 1 : connectionCounts[d.source] + 1 );
            connectionCounts[d.target] = ( typeof connectionCounts[d.target] === 'undefined' ? 1 : connectionCounts[d.target] + 1 );
         });

         _.each(inputData.nodes, function(d, i){
            d.connections = connectionCounts[i];
         });

         link = link.data(force.links(), function(d){ return d.source + "-" + d.target; });
         link.enter().append("line")
            .attr("class", "link")
            .style("stroke-width", function (d) { return Math.sqrt(d.value); });
         link.exit().remove();

         node = node.data(force.nodes()); //, function(d) { return d.id;});
         node.exit().remove();

         var nodeEnter = node.enter().append("g")
            .on("click", function(){
               console.log(arguments);
            })
            .attr("class", "node")
            .attr("id", function (d) { return "N" + parseInt(d.id); })
            .call(force.drag);

         nodeEnter.append("circle")
            .attr("r", 10)
            .style("fill", function (d) { return color(d.node_type); });

         force.linkDistance(function(d){
            if ( d.source.node_type == 'user' && d.source.connections > 1 ) {
               return 10;
            }
            return 80;
         });
         force.linkStrength(function(d){
            if ( d.source.node_type == 'user' && d.source.connections > 1 ) {
               return 0.2;
            }
            return 1;
         });
         force.charge(function(d){
            if ( d.node_type == 'user' && d.connections > 1 ) {
               return -40;
            }
            if ( d.node_type == 'group' ) {
               return -65;
            }
            return -90;
         });

         nodeEnter.append("text")
            .attr("dx", 12)
            .attr("dy", ".35em")
            .text(function (d) {
               if (d.node_type == 'group') {
                  return d.cn;
               } else {
                  return d.name;
               }
            });

         force.start();
         for (var i = 0; i < 100; ++i) force.tick();
      }

      function init(){
         var bounds = getBounds();

         svg = d3.select('#'+config.elementId).append("svg")
            .attr("width", bounds.w)
            .attr("height", bounds.h);

         force = d3.layout.force()
            .nodes(nodes)
            .links(links)
            .gravity(0.01)
            .alpha(0.05)
            .distance(50)
            .charge(-60)
            .size([bounds.w, bounds.h])
            .on('tick', tick)
            .on('start', startForce)
            .on('end', endForce);

         node = svg.selectAll(".node");
         link = svg.selectAll(".link");
      }
      module.init = init;

      function hideLabels(){
         if ( !node ) return;
         node.select('text').style({'opacity': 1, 'visibility': true}).transition().duration(250).style('opacity', 0);
      }
      module.hideLabels = hideLabels;

      function showLabels(){
         if ( !node ) return;
         node.select('text').style({'opacity': 0, 'visibility': true}).transition().duration(250).style('opacity', 1);
      }
      module.showLabels = showLabels;

      function filter(query){
         console.log('filter', query);
      }
      module.filter = filter;

      function load(url){
         $.getJSON(url, function(result){
            inputChange(result);
         });
      }
      module.load = load;

      function buildStats(elementId){
         stats = new Stats();
         stats.setMode(0);
         $('#'+elementId).append(stats.domElement);
      }

      // Start execution
      if ( config.statsElementId ) {
         buildStats(config.statsElementId);
      }
      _.defer(init);

      return module;
   }

   return function(config){
      return Visualizer(_.merge({}, configDefaults, config));
   };

}));
