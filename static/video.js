
var reqURL = "https://api.rss2json.com/v1/api.json?rss_url=" + encodeURIComponent("https://www.youtube.com/feeds/videos.xml?channel_id=");
var apiKey= "AIzaSyBw0otQIxkMX3v4JT9ynJH5s3R9ZULvehY";
var clientId = "691301328864-al5k6cjt1006rgdb4qraus4fm2n7nreu.apps.googleusercontent.com";
var channelID = "UC7WnrV5aBx7LjWp0lorB73Q"
var userID = "7WnrV5aBx7LjWp0lorB73Q"
var bla = reqURL + iframe.getAttribute('cid')
function loadVideo(iframe) {
  $.getJSON(reqURL + iframe.getAttribute('cid'),
    function(data) {
      var videoNumber = (iframe.getAttribute('vnum') ? Number(iframe.getAttribute('vnum')) : 0);
      var link = data.items[videoNumber].link;
      id = link.substr(link.indexOf("=") + 1);
      iframe.setAttribute("src", "https://youtube.com/embed/" + id + "?controls=0&autoplay=1");
      var url = 'https://www.youtube.com/watch?v=' + id;
      // var url = 'https://www.youtube.com/channel/' + videoId + '?view_as=subscriber';
      $.getJSON('https://www.googleapis.com/youtube/v3/videos?id=' + id + '&key=' + apiKey + '&fields=items(snippet(title))&part=snippet', {format: 'json', url: url}, function (data) {
          $("h2").html(data.items[0].snippet.title);

      });
      // $.get("https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + id + "&key=" + apikey, function(data) {
      // data.items[0].snippet.title
      // });
    }
  );
}
// 'https://www.googleapis.com/youtube/v3/videos?id=Gsfb1CbqwkM&key=AIzaSyBw0otQIxkMX3v4JT9ynJH5s3R9ZULvehY&fields=items(snippet(title))&part=snippet'
var iframes = document.getElementsByClassName('latestVideoEmbed');
for (var i = 0, len = iframes.length; i < len; i++) {
  loadVideo(iframes[i]);
}




//
// var reqURL = "https://api.rss2json.com/v1/api.json?rss_url=" + encodeURIComponent("https://www.youtube.com/feeds/videos.xml?channel_id=");
//
// function loadVideo(iframe) {
//   $.getJSON(reqURL + iframe.getAttribute('cid'),
//     function(data) {
//       var videoNumber = (iframe.getAttribute('vnum') ? Number(iframe.getAttribute('vnum')) : 0);
//       console.log(videoNumber);
//       var link = data.items[videoNumber].link;
//       id = link.substr(link.indexOf("=") + 1);
//       iframe.setAttribute("src", "https://youtube.com/embed/" + id + "?controls=0&autoplay=1");
//     }
//   );
// }
//
// var iframes = document.getElementsByClassName('latestVideoEmbed');
// for (var i = 0, len = iframes.length; i < len; i++) {
//   loadVideo(iframes[i]);
// }
