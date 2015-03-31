var generate = angular.module('generate',[]);

generate.directive('pressEnter', function() {
    return function(scope, element, attrs) {
        element.bind("keydown keypress", function(event) {
            if(event.which === 13) {
                scope.$apply(function(){
                    scope.$eval(attrs.pressEnter);
                });
                event.preventDefault();
            }
        });
    };
});

generate.directive('setFocus', function() {
  return function(scope, element, attrs) {
      element[0].focus(); 
      };
});
