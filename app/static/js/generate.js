generate.controller('generateFilesControl',['$scope','$http',function($scope, $http){
    $scope.fileContents = "Text to save";
    $scope.generateDoc  = "Generate file";
    $scope.contents     = null;
    $scope.filename     = null;
    $scope.fileURL      = config.apiURL;
    $scope.extension    = config.extension;

    $scope.clearForm = function(){
        $scope.contents = null;
    };
   
    $scope.clearAlert = function(){
        $scope.clearForm();
        $scope.alert    = null;
        $scope.filename = null;
    };

    $scope.generateDocument = function(){
        var new_document = {
            'contents': $scope.contents
        };
        $scope.url = config.apiURL + "/generate/insert";
        $http({
                 method:  'POST',
                 url:     $scope.url,
                 data:    new_document,
                 headers: {'ContentType': 'application/json'}
        }).then(
            function(data){
                    $scope.alert    = 'document generated: ';
                    $scope.filename = data.data;
                    $scope.fileURL  = config.apiURL + "/generate/download/" + $scope.filename + $scope.extension;
                    console.log(data);
                    $scope.clearForm();
            },
            function(){
                $scope.alert = 'failed to generate document';
        });
    };
}]);
