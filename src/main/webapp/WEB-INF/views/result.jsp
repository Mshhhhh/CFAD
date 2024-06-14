<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile Cards</title>
    <link rel="stylesheet" href="${pageContext.request.contextPath}\resources\css\rstyle.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
</head>
<body>
    <header class="header">
        <div>
            <a href="${pageContext.request.contextPath}\">
                <img src="${pageContext.request.contextPath}\resources\images\logo.png" alt="Logo">
            </a>
        </div>

    </header>

    <!-- 메시지 영역 추가 -->
    <div class="message-container">
        <div class="username" id="displayName">님, 이런 칵테일은 어때요?</div>
    </div>

    <div class="card-container" id="captureArea">
    <c:forEach var="cocktail" items="${id_cocktails}">
        <div class="card">
            <img src="${pageContext.request.contextPath}/resources/cocktail_image/${cocktail.cocktail_name_en}.jfif" alt="Profile Image" crossorigin="anonymous">
            <h2>${cocktail.cocktail_name_en}</h2>
            <p class="short-info">${cocktail.cocktail_name_kr}</p>
            <p class="more-info">${cocktail.alcohol}%</p>
            <p class="more-info1">${cocktail.cocktail_ingredient_en}(${cocktail.cocktail_ingredient_kr})</p>
        </div>
    </c:forEach>
    </div>

    <div id="emailModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <form id="emailForm" onsubmit="sendEmail(event)">
                <label for="email">이메일을 입력하세요:</label>
                <input type="email" id="email" name="email" required>
                <textarea id="message" name="message" placeholder="메시지를 입력하세요" required></textarea>
                <input type="hidden" id="imageData" name="imageData">
                <button type="submit">보내기</button>
            </form>
        </div>
    </div>

    <script>
        function captureAndShare() {
            html2canvas(document.querySelector("#captureArea"), { useCORS: true }).then(canvas => {
                canvas.style.display = 'none';
                document.body.appendChild(canvas);
                const imageData = canvas.toDataURL("image/png");
                document.getElementById('imageData').value = imageData;
                document.getElementById('emailModal').style.display = 'block';
            }).catch(err => {
                console.error('캡처에 실패했습니다:', err);
                alert('캡처에 실패했습니다. 이미지 로드 시 문제가 발생했습니다.');
            });
        }

        function closeModal() {
            document.getElementById('emailModal').style.display = 'none';
        }

        function sendEmail(event) {
            event.preventDefault();
            const formData = new FormData(document.getElementById('emailForm'));

            fetch('https://script.google.com/macros/s/AKfycbzqu4XXDFOv2Lj5BrYewOnvahrdrl_apZcIl0mmRZ0LORzKcL6DJWFIhhtIKWzqzuZN/exec', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(data => {
                alert('메일이 전송되었습니다!');
                closeModal();
            })
            .catch(error => {
                alert('메일 전송에 실패했습니다: ' + error);
            });
        }

        document.addEventListener('DOMContentLoaded', function() {
            const username = localStorage.getItem('username');
            const mood = localStorage.getItem('mood') || '좋'; // Replace '좋' with the actual mood value
            if (username) {
                document.getElementById("displayName").innerText = username + '님, 이런 칵테일은 어때요?' ;
            }
        });
    </script>
</body>
</html>
