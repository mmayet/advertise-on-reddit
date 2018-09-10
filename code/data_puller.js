var redditSubModule = 'mildlyinfuriating';
var http = require('http');

function getRedditPosts() {
    var url = 'http://www.reddit.com/r/' + redditSubModule + '/new/.json';

    var request = http.get(url, function (response) {
        var json = '';
        response.on('data', function (chunk) {
            json += chunk;
        });

        response.on('end', function () {
            var redditResponse = JSON.parse(json);
            redditResponse.data.children.forEach(function (child) {
                if (child.data.domain !== 'self.node') {
                    console.log('-------------------------------');
                    console.log('Author : ' + child.data.author);
                    console.log('Domain : ' + child.data.domain);
                    console.log('Title : ' + child.data.title);
                    console.log('URL : ' + child.data.url);
                }
            });
        })
    });
    request.on('error', function (err) {
        console.log(err);
    });
}

getRedditPosts();
