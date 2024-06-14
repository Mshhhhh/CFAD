<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CFAD_Cocktail </title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}\resources\css\style.css" />

</head>
<body>
    <header class="header">
        <div>
            <a href="/">
            <img src="${pageContext.request.contextPath}\resources\images\logo.png" alt="Logo"></a>
        </div>
        <nav class="nav">
        </nav>
    </header>
    <main class="main-content">
        <div class="text">
            <h1>Facial<br>Recognition<br><span class="hilghlight">Cocktail</span></h1></span>
            <button onclick="location.href='${pageContext.request.contextPath}/select'">Try Now</button>
        </div>

        <div class="image-container">
            <img src="${pageContext.request.contextPath}\resources\images\home_img.png" alt="Cocktail Image">
        </div>
    </main>
</body>
</html>