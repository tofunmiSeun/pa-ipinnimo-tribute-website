var app = angular.module('funeral-tribute', ['ui.router']);
app.constant('SERVER_URL', 'http://localhost:1967/api');

/*
app.service('Session', function () {
    this.create = function (userObject) {
        this.userObject = userObject;
    };
    this.destroy = function () {
        this.userObject = null;
    };
    this.isAdmin = function () {
        return this.userObject.isAdmin;
    }
});

app.factory('AuthService', function ($http, Session, SERVER_URL) {
    var authService = {};

    authService.login = function (credentials) {

        var successHandler = function (response) {
            var userObject = response.data;
            Session.create(userObject.user);
            return userObject;
        };

        var errorHandler = function () {
            return {errorMessage: "An error occurred while trying to login. Try again"};
        };

        return $http.post(SERVER_URL + '/login', credentials).then(successHandler, errorHandler)
    };

    authService.logout = function () {
        Session.destroy();
    };

    authService.isAuthenticated = function () {
        return !!Session.userObject;
    };

    authService.isAdmin = function () {
        return (authService.isAuthenticated() && Session.isAdmin());
    };

    return authService;
});

app.run(function ($rootScope, $state, AuthService) {
    $rootScope.$on('$stateChangeStart', function (event, next) {
        if (next.data.requiresLogin && next.data.requiresAdmin && !AuthService.isAdmin()) {
            event.preventDefault();
            $state.transitionTo('home.courses');
        } else if (next.data.requiresLogin && !AuthService.isAuthenticated()) {
            event.preventDefault();
            $state.transitionTo('login');
        }
    });
});
*/
