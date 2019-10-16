var app = angular.module("nvd3App", []);

function readBody(xhr) {

    if (xhr.responseText) {
        return xhr.responseText;
    }

}

function addfield() {
    if (document.getElementsByName("bname")[document.getElementsByName("bname").length - 1].value == "") {

        alert("Please complete the available form before adding a new one.");
        document.getElementsByName("bname")[document.getElementsByName("bname").length - 1].focus();

    } else if (document.getElementsByName("burl")[document.getElementsByName("burl").length - 1].value == "") {

        alert("Please complete the available form before adding a new one.");
        document.getElementsByName("burl")[document.getElementsByName("burl").length - 1].focus();

    } else if (document.getElementsByName("btitle")[document.getElementsByName("btitle").length - 1].value == "") {

        alert("Please complete the available form before adding a new one.");
        document.getElementsByName("btitle")[document.getElementsByName("btitle").length - 1].focus();

    } else {
        var newDiv =
            "<div style='background-color: aliceblue;border-radius: 7px;' class='getall'>" +
            "<br> Enter business name: <input type='text' name = 'bname' class='form-control' placeholder='Business name' required>" +
            " Enter sample product URL <input type='text' name = 'burl' class='form-control' placeholder='URL' required>" +
            " Enter sample product Title <input type='text' name = 'btitle' class='form-control' placeholder='Title' required>" +
            " <input type='button' name='delb' class='btn btn-success' value='delete' onclick='deldiv(this)'><br></div>"
        let doc = new DOMParser().parseFromString(newDiv, "text/html");
        document.getElementById("div1").appendChild(doc.documentElement.getElementsByTagName("div")[0]);
        document.getElementsByName("bname")[document.getElementsByName("bname").length - 1].focus();
    }
}

function deldiv(delbutton) {

    delbutton.parentElement.outerHTML = "";

}

function sub() {

    if (document.getElementById("form1").checkValidity()) {

        var getall = document.getElementsByClassName("getall");
        if (getall.length > 0) {

            allbus = [];

            for (var i = 0; i <= getall.length - 1; i++) {

                inputs = getall[i].children;

                var buslist = {};

                for (var j = 0; j < inputs.length; j++) {

                    if (inputs[j].tagName == "INPUT" && inputs[j].type == "text" || inputs[j].type == "url") {

                        buslist[inputs[j].name] = inputs[j].value;

                    }

                }
                allbus.push(buslist)
            }
        }

        if (allbus) {
            var xhr = new XMLHttpRequest();
            xhr.open("POST", window.location.href, true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify(allbus));
            flag = 1;
            xhr.onreadystatechange = function () {

                if (readBody(xhr) && flag == 1) {
                    flag = 2;
                    var modalObj = JSON.parse(readBody(xhr));
                    document.getElementById("info").innerHTML = modalObj.modalMesage;
                    document.getElementById("openadd").click();
                    console.log(modalObj.modalMesage);
                }
            }

            var count = 0;

            if (document.getElementsByName("delb").length > 0) {
                count = 1
            }

            while (count == 1) {

                document.getElementsByName("delb")[0].click();

                if (document.getElementsByName("delb").length > 0) {
                    count = 1
                } else {

                    count = 0;

                }

            }



            getall = document.getElementsByClassName("getall");

            if (getall.length > 0) {

                for (var i = 0; i <= getall.length - 1; i++) {

                    inputs = getall[i].children;

                    var buslist = {};

                    for (var j = 0; j < inputs.length; j++) {

                        if (inputs[j].tagName == "INPUT" && inputs[j].type == "text" || inputs[j].type == "url") {

                            inputs[j].value = "";

                        }

                    }
                }
            }
        }
    }
}


var app = angular.module('nvd3App', ['nvd3']);

app.controller('MainCtrl', function ($scope, $timeout, $http) {


    $scope.subkey = function (subkeyword) {
        if (document.getElementById("form2").checkValidity()) {

            $http({
                method: 'POST',
                url: window.location.href + "keyword",
                data: {
                    "keyword": subkeyword
                }


            }).then(function (response) {

                $scope.showSearchhide = false;

                document.getElementById("root1").remove();
                document.getElementById("root").remove();

                var newDiv = "<div id='root'></div>";
                let doc = new DOMParser().parseFromString(newDiv, "text/html");
                document.getElementById("refresh").appendChild(doc.documentElement.getElementsByTagName("div")[0]);

                var newDiv2 = "<div class='pages' id='root1'></div>";
                let doc2 = new DOMParser().parseFromString(newDiv2, "text/html");
                document.getElementById("refresh").appendChild(doc2.documentElement.getElementsByTagName("div")[0]);

                if (response.data) {

                    if (response.data.modalMesage) {
                        document.getElementById("info").innerHTML = response.data.modalMesage;
                        document.getElementById("openadd").click();

                    } else if (response.data.result) {

                        var data = [];

                        for (i in response.data.result) {

                            data[i] = {};

                            data[i].brand = response.data.result[i][1];
                            data[i].model = response.data.result[i][2];
                            data[i].price = response.data.result[i][3];
                            data[i].stock = response.data.result[i][4];
                            data[i].producturl = response.data.result[i][5];
                            data[i].condition = response.data.result[i][6];
                            data[i].category = response.data.result[i][7];

                        }

                        if (data) {
                            $scope.showSearchhide = true;

                            var columns = {
                                'brand': 'Brand',
                                'model': 'Model',
                                'price': 'Price',
                                'stock': 'Stock',
                                'producturl': 'Product URL',
                                'condition': 'Condition',
                                'category': 'Category'
                            }

                            var TestData = {
                                data: data,
                                columns: columns
                            }

                            var table = $('#root').tableSortable({
                                data: TestData.data,
                                columns: TestData.columns,
                                dateParsing: true,
                                processHtml: function (row, key) {
                                    if (key === 'producturl') {
                                        return '<a href="' + row[key] + '" target="_blank">View product</a>'
                                    }
                                    return row[key]
                                },
                                columnsHtml: function (value, key) {
                                    return value;
                                },
                                pagination: 5,
                                showPaginationLabel: true,
                                prevText: 'Prev',
                                nextText: 'Next',
                                searchField: $('#search'),
                                responsive: [{
                                        maxWidth: 992,
                                        minWidth: 769,
                                        columns: TestData.col,
                                        pagination: true,
                                        paginationLength: 3
                                    },
                                    {
                                        maxWidth: 768,
                                        minWidth: 0,
                                        columns: TestData.colXS,
                                        pagination: true,
                                        paginationLength: 2
                                    }
                                ]
                            })
                        }

                    }
                }

            })

            document.getElementById("search").value = "";
        }

    }

    // $http.get(window.location.href + "viz")
    // .then(function(response) {
    //     console.log(response.data);

    //     $timeout(function () {

    //         $scope.options = {
    //             chart: {
    //                 type: 'pieChart',
    //                 showLegend: true,
    //                 labelType: function(d){
    //                     var percent = (d.endAngle - d.startAngle) / (2 * Math.PI);
    //                     return d3.format('.2%')(percent);
    //                 },
    //                 height: 500,
    //                 x: function (d) {
    //                     return d.key;
    //                 },
    //                 y: function (d) {
    //                     return d.y;
    //                 },
    //                 showLabels: true,
    //                 duration: 500,
    //                 labelThreshold: 0.01,
    //                 labelSunbeamLayout: true,
    //                 legend: {
    //                     margin: {
    //                         top: 5,
    //                         right: 35,
    //                         bottom: 5,
    //                         left: 0
    //                     }
    //                 }
    //             }
    //         };

    //         $scope.data = [{
    //                 key: "One",
    //                 y: 5
    //             },
    //             {
    //                 key: "Two",
    //                 y: 2
    //             },
    //             {
    //                 key: "Three",
    //                 y: 9
    //             },
    //             {
    //                 key: "Four",
    //                 y: 7
    //             },
    //             {
    //                 key: "Five",
    //                 y: 4
    //             },
    //             {
    //                 key: "Six",
    //                 y: 3
    //             },
    //             {
    //                 key: "Seven",
    //                 y: .5
    //             }
    //         ];

    //     }, 1);

    //     $timeout(function () {

    //         $scope.options2 = {
    //             chart: {
    //                 type: 'discreteBarChart',
    //                 height: 450,
    //                 showLegend: true,
    //                 margin: {
    //                     top: 20,
    //                     right: 20,
    //                     bottom: 50,
    //                     left: 55
    //                 },
    //                 x: function (d) {
    //                     return d.label;
    //                 },
    //                 y: function (d) {
    //                     return d.value + (1e-10);
    //                 },
    //                 showValues: true,
    //                 valueFormat: function (d) {
    //                     return d3.format(',.4f')(d);
    //                 },
    //                 duration: 500,
    //                 xAxis: {
    //                     axisLabel: 'X Axis'
    //                 },
    //                 yAxis: {
    //                     axisLabel: 'Y Axis',
    //                     axisLabelDistance: -10
    //                 }
    //             }
    //         };

    //         $scope.data2 = [{
    //             key: "Cumulative Return",
    //             values: [{
    //                     "label": "C",
    //                     "value": 32.807804682612
    //                 },
    //                 {
    //                     "label": "D",
    //                     "value": 196.45946739256
    //                 }
    //             ]
    //         }]
    //     }, 1);

    //     $timeout(function () {
    //             window.dispatchEvent(new Event('resize'));
    //     }, 100);


    // });


});