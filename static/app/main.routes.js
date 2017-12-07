app.config(['$stateProvider', '$urlRouterProvider',

    function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise("/home");

        $stateProvider
            .state('home', {
                url: '/login',
                templateUrl: 'static/app/modules/login/login.html',
                data: {requiresLogin: false}
            })
    }
]);