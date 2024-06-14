<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CFAD</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}\resources\css\nstyle.css"/>
</head>
<body>
    <header class="header">
        <div>
            <a href="${pageContext.request.contextPath}/">
                <img src="${pageContext.request.contextPath}\resources\images\logo.png" alt="Logo">
            </a>
        </div>
        <nav class="nav">
        </nav>
    </header>

    <div class="container">
        <div class="image-panel">
            <img src="${pageContext.request.contextPath}\resources\images\wink.gif" alt="Profile Image" class="profile-image">
        </div>
        <div class="name-panel">
            <form id="nameForm" onsubmit="return setName()">
                <label for="username" >이름을 입력하세요:</label>
                <input type="text" id="username" name="username" required>
                <button type="submit" class="next-btn">확인</button>
            </form>
        </div>
    </div>
    
    <div class="slider-wrapper" style="display: none;">
        <button id="prev">
            <img src="${pageContext.request.contextPath}\resources\images\icon_left.png" alt="left">
        </button>
        <div class="slider-container">
            <div class="slider">
                <!-- Clone of the last slide for infinite loop effect -->
                <div class="slide clone">
                    <div class="rectangle">
                        <div class="content">
                            <img src="${pageContext.request.contextPath}\resources\images\icon_ai.gif" alt="Image" class="rectangle-image">
                            <p class="text">AI 바텐더</p>
                            <button class="action-btn">
                                <a href="${pageContext.request.contextPath}/cameraws" class="action-link">START</a>
                            </button>
                        </div>
                    </div>
                </div>
                <!-- Actual slides -->
                <div class="slide">
                    <div class="rectangle">
                        <div class="content">
                            <img src="${pageContext.request.contextPath}\resources\images\icon_face.gif" alt="Image" class="rectangle-image">
                            <p class="text">감정 인식</p>
                            <button class="action-btn">
                                <a href="${pageContext.request.contextPath}/camera" class="action-link">START</a>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="slide">
                    <div class="rectangle">
                        <div class="content">
                            <img src="${pageContext.request.contextPath}\resources\images\icon_select.gif" alt="Image" class="rectangle-image">
                            <p class="text">선호도 조사</p>
                            <button class="action-btn">
                                <a href="${pageContext.request.contextPath}/survey1" class="action-link">START</a>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="slide">
                    <div class="rectangle">
                        <div class="content">
                            <img src="${pageContext.request.contextPath}\resources\images\icon_ai.gif" alt="Image" class="rectangle-image">
                            <p class="text">AI 바텐더</p>
                            <button class="action-btn">
                                <a href="${pageContext.request.contextPath}/cameraws" class="action-link">START</a>
                            </button>
                        </div>
                    </div>
                </div>
                <!-- Clone of the first slide for infinite loop effect -->
                <div class="slide clone">
                    <div class="rectangle">
                        <div class="content">
                            <img src="${pageContext.request.contextPath}\resources\images\icon_face.gif" alt="Image" class="rectangle-image">
                            <p class="text">감정 인식</p>
                            <button class="action-btn">START</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <button id="next">
            <img src="${pageContext.request.contextPath}\resources\images\icon_right.png" alt="right">
        </button>
    </div>
    <div class="dots" style="display: none;">
        <span class="dot active" data-index="0"></span>
        <span class="dot" data-index="1"></span>
        <span class="dot" data-index="2"></span>
    </div>

    <script src="${pageContext.request.contextPath}\resources\js\nscript.js"></script>
</body>
</html>
