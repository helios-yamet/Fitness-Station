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

//credit to google developer documentation
var locations = [
	//code adapted from google developers
	["Fitness Station", 51.2022171, -3.4670381,17, 2],
];
var map;
//create map object
function initMap() {
	map = new google.maps.Map(document.getElementsByClassName("map-custom")[0], {
		center: {
			lat: 51.2022171,
			lng: -3.4670381,17
		},
		zoom: 9
	});

	//call map window& create marker variable
	var infowindow = new google.maps.InfoWindow();

	var marker, i;

	for (i = 0; i < locations.length; i++) {
		marker = new google.maps.Marker({
			position: new google.maps.LatLng(locations[i][1], locations[i][2]),
			map: map
		});

		//add event listener, set markers to locations
		google.maps.event.addListener(marker, "click", (function (marker, i) {
			return function () {
				infowindow.setContent(locations[i][0]);
				infowindow.open(map, marker);
			};
		})(marker, i));
	}
}