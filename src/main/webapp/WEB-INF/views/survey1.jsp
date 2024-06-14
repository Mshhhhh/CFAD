<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CFAD</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}\resources\css\sstyle.css">
</head>

<body>

        <header class="header">
            <div>
                <a href="${pageContext.request.contextPath}\">
                <img src="${pageContext.request.contextPath}\resources\images\logo.png" alt="Logo"></a>
            </div>
            <nav class="nav">
            </nav>
        </header>
        
        <main>
            <div class="left-panel">

                <div id="emojiSelection">
                    <h2 id="greeting"></h2>
                    <div class="emoji-container">
                        <div class="emoji" onclick="selectEmoji('emoji1')">😍</div>
                        <div class="emoji" onclick="selectEmoji('emoji2')">😎</div>
                        <div class="emoji" onclick="selectEmoji('emoji3')">🧙‍♂️</div>
                        <div class="emoji" onclick="selectEmoji('emoji4')">😈</div>
                        <div class="emoji" onclick="selectEmoji('emoji5')">😡</div>
                        <div class="emoji" onclick="selectEmoji('emoji6')">😐</div>
                        <div class="emoji" onclick="selectEmoji('emoji7')">😊</div>
                        <div class="emoji" onclick="selectEmoji('emoji8')">💀</div>
                    </div>
                    <button class="next-btn" onclick=nextPage()>다음으로</button>
                </div>
            </div>
            <div class="right-panel">
                <div class="card">
                    <div class="selected-emoji" id="selectedEmoji">⚪</div>
                    <div class="username" id="displayName">이름</div>
                </div>
            </div>
        </main>
    </div>
    <script src="${pageContext.request.contextPath}\resources\js\sscript.js"></script>
    <script>function nextPage() {
        window.location.href = "${pageContext.request.contextPath}/survey2";
    }</script>
</body>
</html>
