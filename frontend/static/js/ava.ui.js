/**
 * AVA D3 Visualizer
 * @module AVA.UI
 */
/* jshint unused: false, newcap: false */
(function (root, factory) {
   // UMD Header. https://github.com/umdjs/umd
   if (typeof define === 'function' && define.amd) { var dependencies = []; define(dependencies, factory); }
   else if (typeof exports === 'object') { module.exports = factory(); }
   else {
      if ( typeof root.AVA === 'undefined' ) { root.AVA = {}; }
      root.AVA.UI = factory();
   }
}(this, function(){

   var module = {};

   var AdhocButtonsConfigDefaults = {
      'buttonContainer': false,
      'buttonTmpl': _.template('<button type="button" class="btn btn-default btn-sm filter-button"><%= label %></button>')
   };

   function AdhocButtons(config){

      var buttons = false;

      function onFilterClicked(e){
         var button = buttons.find({'element': this}).value();
         var element = $(this);
         if ( button.type === 'toggle' ) {
            // Toggle button
            element.toggleClass('active');
            if ( element.hasClass('active') ) {
               button.on(element, e);
            } else {
               button.off(element, e);
            }
         } else {
            // Normal button
            button.action(element, e);
         }
      }

      function add(buttonList){
         buttons = _.chain(buttonList);
         buttons.each(function(button){
            var templateParams = button;
            var element = $(config.buttonTmpl(templateParams));
            button.element = element.appendTo(config.buttonContainer).get(0);
            if ( typeof button['default'] === 'string' ) {
               button.type = 'toggle';
               _.defer(function(){
                  if ( button.default === 'off' ) { // Flip the onFilterClicked correctly
                     button.addClass('active');
                  }
                  onFilterClicked.call(button.element, null);
               });
            } else {
               button.type = 'normal';
            }
         });
         $('button', config.buttonContainer).on('click', onFilterClicked);
      }

      return {
         'add': add
      };
   }

   module.AdhocButtons = function(config){
      return AdhocButtons(_.merge({}, AdhocButtonsConfigDefaults, config));
   };

   var filterGroupConfigDefaults = {
      'filterGroupContainer': false,
      'onFilterGroupClicked': function(group, allGroups){},
      'labelNameCallback': function(group) { return group.cn; },
      'checkboxTmpl': _.template('<label class="checkbox-inline filter-label"><input type="checkbox" id="<%= node.id %>" data-groupid="<%= node.id %>" checked><%= label %></label>')
   };

   function FilterGoups(config){

      var module = {};

      var allGroups = {};

      function onFilterGroupClicked(e){
         var element = $(this);
         var id = element.data('groupid');
         var group = allGroups[id];
         if (group) {
            group.show = element.is(':checked');
            config.onFilterGroupClicked(group, allGroups, e);
         }
      }

      function toCheckboxHtml(node){
         return {
            'check': config.checkboxTmpl({node: node, label: config.labelNameCallback(node)}),
            'node': node
         };
      }

      function onDataUpdated(nodes){
         allGroups = {};
         _.chain(nodes)
            .filter({'node_type': 'group'})
            .map(toCheckboxHtml)
            .each(function(pair){
               allGroups[pair.node.id] = _.extend({}, pair.node, {'show': true});
               config.filterGroupContainer.append(pair.check);
            });
         $('input', config.filterGroupContainer).on('click', onFilterGroupClicked);
      }
      module.onDataUpdated = onDataUpdated;

      return module;
   }

   module.FilterGroups = function(config){
      return FilterGoups(_.merge({}, filterGroupConfigDefaults, config));
   };

   return module;

}));
