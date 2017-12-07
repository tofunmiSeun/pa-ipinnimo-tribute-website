app.controller('tributesController', ['$scope', '$state', 'tributesService',
    function ($scope, $state, tributesService) {

        $scope.allTributes = [];
        $scope.newTributeObject = {
            name: "",
            content: ""
        };

        $scope.init = function () {
            $scope.clearAllMessages();
            $scope.getTributes();
        };

        $scope.getTributesLoading = true;
        $scope.getTributes = function () {
            $scope.clearAllMessages();
            $scope.getTributesLoading = true;

            var successHandler = function (response) {
                $scope.allTributes = response.data;
                $scope.getTributesLoading = false;
            };

            var errorHandler = function (response) {
                $scope.setErrorMessage("Error trying to get courses.");
                $scope.getTributesLoading = false;
                console.log(response)
            };

            tributesService.getAllTributes(successHandler, errorHandler);
        };


        /* ERROR AND SUCCESS MESSAGES */

        $scope.successMessage = null;
        $scope.errorMessage = null;

        $scope.setSuccessMessage = function (message) {
            $scope.successMessage = message;
        };
        $scope.clearSuccessMessage = function () {
            $scope.successMessage = null;
        };
        $scope.setErrorMessage = function (message) {
            $scope.errorMessage = message;
        };
        $scope.clearErrorMessage = function () {
            $scope.errorMessage = null;
        };

        $scope.clearAllMessages = function () {
            $scope.clearSuccessMessage();
            $scope.clearErrorMessage();
        };
    }]);

app.service('tributesService', ['$http', 'SERVER_URL', function ($http, SERVER_URL) {
    this.getAllTributes = function (successHandler, errorHandler) {
        $http.get(SERVER_URL + '/tributes/all').then(successHandler, errorHandler);
    }
}]);