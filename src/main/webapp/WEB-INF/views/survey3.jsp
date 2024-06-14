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
                <div class="emoji" onclick="selectEmoji('emoji1', 0, 'sweet')">🍭</div>
                <div class="emoji" onclick="selectEmoji('emoji2', 1, 'bitter')">😖</div>
                <div class="emoji" onclick="selectEmoji('emoji3', 2, 'citrusy')">🍍</div>
                <div class="emoji" onclick="selectEmoji('emoji4', 3, 'sour')">🍋</div>
                <div class="emoji" onclick="selectEmoji('emoji5', 4, 'spicy')">🔥</div>
                <div class="emoji" onclick="selectEmoji('emoji6', 5, '상관없어요!')">🤷‍♂️</div>
            </div>
            <button class="next-btn" onclick=nextPage()>결과보기</button>
        </div>
    </div>
    <div class="right-panel">
        <div class="card">
            <div class="selected-emoji" id="selectedEmoji">⚪</div>
            <div class="username" id="displayName"></div>
        </div>
    </div>
</main>
</div>
<script src="${pageContext.request.contextPath}\resources\js\sscript3.js"></script>
<script>function nextPage() {
    var alcoholvalue = sessionStorage.getItem('alcoholvalue');
    var tastevalue = window.tastevalue;
    window.location.href = "${pageContext.request.contextPath}/result?alcohol=" + alcoholvalue + "&taste=" + tastevalue;
}</script>
</body>
</html>
