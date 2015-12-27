/**
 * Lodash / Underscore method for breaking data sets into smaller sets (chunks)
 *
 * @arguments
 *
 *  collection: Array / Object
 *  chuckSize:  Number
 *
 * @example
 *
 * -> _.chunk(["number","array_element","city_prefix","city_suffix","street_suffix"], 3));
 * -> [["number","array_element","city_prefix"], ["city_suffix","street_suffix"]]
 */

_.mixin({
  'chunk': function (collection, chunkSize) {
    if (!collection || _.isNaN(parseInt(chunkSize, 10))) { return [];}
    return _.toArray(_.groupBy(collection, function (iterator, index) {
      return Math.floor(index / parseInt(chunkSize, 10));
    }));
  }
});
