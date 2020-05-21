
var reqURL = "https://api.rss2json.com/v1/api.json?rss_url=" + encodeURIComponent("https://www.youtube.com/feeds/videos.xml?channel_id=");
var apiKey= "AIzaSyBw0otQIxkMX3v4JT9ynJH5s3R9ZULvehY";
var channelID = "UC7WnrV5aBx7LjWp0lorB73Q"

function loadVideo(iframe) {
  $.getJSON(reqURL + iframe.getAttribute('cid'),
    function(data) {
      var videoNumber = (iframe.getAttribute('vnum') ? Number(iframe.getAttribute('vnum')) : 0);
      var link = data.items[videoNumber].link;
      id = link.substr(link.indexOf("=") + 1);
      iframe.setAttribute("src", "https://youtube.com/embed/" + id + "?controls=0&autoplay=0");

      var url = 'https://www.youtube.com/channel/' + channelID;
      $.getJSON('https://www.googleapis.com/youtube/v3/videos?id=' + id + '&key=' + apiKey + '&fields=items(snippet(title))&part=snippet', {format: 'json', url: url}, function (data) {
        var h2s = $("h2")
        console.log(data.items)
        $(h2s[videoNumber]).html(data.items[0].snippet.title)
        
      });
    }
  );
}

var iframes = document.getElementsByClassName('latestVideoEmbed');
for (var i = 0, len = iframes.length; i < len; i++) {
  loadVideo(iframes[i]);
}

console.log('hello');
