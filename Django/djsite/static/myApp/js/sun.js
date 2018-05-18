$(document).ready(function () {
    document.getElementById("btn").onclick=
        function (ev) {
        $.ajax({
            type:"get",
            url:'/sun/studentsinfo/',
            dataType:'json',
            success:function (data, status) {
                console.log(data)

                var d = data["data"]
                for (var i = 0; i < d.length; ++i) {
                    document.write('<p>' + d[i][0]+ " " + d[i][1] + '</p>')
                }
            }
        })
        }

})