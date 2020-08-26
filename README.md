# askme
Ask Me BOT

## Get started
Run following commands
`cd e:\git\prakashdale\askme`

`conda activate rasasrc`

`rasa run --enable-api --cors "*"`

## Webchat frontend
https://github.com/botfront/rasa-webchat
https://botfront.io/docs/getting-started/setup

Following script added to _layouts\page.html of prakashdale.github.io

```javascript
<script src="https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.min.js"></script>
// you can add a version tag if you need, e.g for version 0.11.5 https://cdn.jsdelivr.net/npm/rasa-webchat@0.11.5/lib/index.min.js
<script>
  WebChat.default.init({
    selector: "#webchat",
    customData: {"language": "en"}, // arbitrary custom data. Stay minimal as this will be added to the socket
    socketUrl: "http://localhost:5005",
    socketPath: "/socket.io/",
    title: "Askme",
    subtitle: "I am a BOT",
    params: {"storage": "session"} // can be set to "local"  or "session". details in storage section.
  })
</script>
```

