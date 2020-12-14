// Read more button
function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");
    
    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more";
        moreText.style.display = "none";
      } else {
          dots.style.display = "none";
          btnText.innerHTML = "Read less";
          moreText.style.display = "inline";
        }
    }


// Enquiries form
//Modified from Code Institute Module @ https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+IFD101+2017_T3/courseware/03d3f6524ad249d9b33e3336d156dfd0/e4710f80cdf34bffbd607bc102482d5c/?activate_block_id=block-v1%3ACodeInstitute%2BIFD101%2B2017_T3%2Btype%40sequential%2Bblock%40e4710f80cdf34bffbd607bc102482d5c
function sendMail(contactForm) {
  emailjs
    .send("gmail", "michodgs", {
      from_name: contactForm.name.value,
      from_email: contactForm.emailaddress.value,
      message_request: contactForm.message.summary.value,
    })
    //custom alert from https://sweetalert.js.org/
    .then(
      function response (response) {
          swal({
      title: "Thanks for reaching out!",
      text: "I'll be in touch",
      icon: "success",
      button: "All Done",
    });
      },
      function (error) {
        swal({
          title: "Sorry, that message didn't send",
          text: "Please try again",
          icon: "error",
          button: "OK",
        });
      }
    );
  $("#formContact").val("");
  $('#formContact input[type="text"]').val("");
  $('#formContact input[type="email"]').val("");
  $("#formContact textarea").val("");
  return false; // To block from loading a new page
}