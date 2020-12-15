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

//GOOGLE MAPS
// Initialize and add the map
function initMap() {
  
// My location
  var homePin = { lat: 51.2022171, lng: -3.4670381,17 
};
  
// The map, centered at home
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 10,
    center: homePin,
  };

  //zoom reset code and marker animation taken from google documentation:https://developers.google.com/maps/documentation/javascript/events#MarkerEvents
  map.addListener("center_changed", () => {
    window.setTimeout(() => {
      map.panTo(marker.getPosition());
    }, 2000);
  });
  var marker = new google.maps.Marker({
    position: homePin,
    map: map,
    animation: google.maps.Animation.DROP,
  });
  marker.addListener("click", () => {
    map.setZoom(16);
    map.setCenter(marker.getPosition());
    infoWindow.open(map, marker);
  });
}
