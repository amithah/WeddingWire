$(function () {

    function reloadPage() {
        location.reload(true);
    }


    Dropzone.options.myAwesomeDropzone = {
        paramName: "file", // The name that will be used to transfer the file
        maxFilesize: 2, // MB
        // accept: function(file, done) {
        //   if (file.name == "justinbieber.jpg") {
        //     done("Naha, you don't.");
        //   }
        //   else {
        //       done();
        //
        //   }
        // },
        success: function (file, response) {
            if (response) {
                // alert("updating bride image");
                brideImagePath = response['uploaded_path'];
            }

        }
    };

    Dropzone.options.groomDropzone = {
        paramName: "file", // The name that will be used to transfer the file
        maxFilesize: 2, // MB
        // accept: function(file, done) {
        //   if (file.name == "justinbieber.jpg") {
        //     done("Naha, you don't.");
        //   }
        //   else {
        //       done();
        //
        //   }
        // },
        success: function (file, response) {
            if (response) {
                // alert("updating groom image");
                groomImagePath = response['uploaded_path'];
            }

        }
    };

    // save bride image to db on button press
    $("#brideImageSubmit").click(function () {
        if (brideImagePath != "") {
            // alert( "Saving" + brideImagePath + "to db ....." );
            $.ajax({
                type: "POST",
                url: ImageSubmitUrl,
                data: {
                    "image_type": "bride_img",
                    "uploaded_path": brideImagePath
                }, // serializes the form's elements.
                success: function (data) {
                    // alert(data); // show response from the php script.
                    $('#modal_image').modal('toggle');
                    reloadPage();

                }
            });
        } else {
            alert(" Please upload a image first");

        }

    });
    // save groom image to db on button press
    $("#groomImageSubmit").click(function () {
        if (groomImagePath != "") {
            $.ajax({
                type: "POST",
                url: ImageSubmitUrl,
                data: {
                    "image_type": "groom_img",
                    "uploaded_path": groomImagePath
                }, // serializes the form's elements.
                success: function (data) {
                    // alert(data); // show response from the php script.
                    $('#modal_image_groom').modal('toggle');
                    reloadPage();
                }
            });
        } else {
            alert(" Please upload a image first for groom");

        }

    });

    // this is the id of the form
    $("#contentForm").submit(function (e) {

        e.preventDefault(); // avoid to execute the actual submit of the form.
        var form = $(this);
        var url = form.attr('action');

        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(), // serializes the form's elements.
            success: function (data) {
                // alert(data); // show response from the php script.
                $('#modal_content').modal('toggle');
                reloadPage();

            }
        });


    });
});