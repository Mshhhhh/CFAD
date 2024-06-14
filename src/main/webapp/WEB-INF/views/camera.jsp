<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capture and Analyze Photo</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"
            integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
            crossorigin="anonymous"></script>

    <link rel="stylesheet" href="${pageContext.request.contextPath}\resources\css\sstyle.css">
</head>


<body>
    <header class="header">
        <div>
            <a href ="${pageContext.request.contextPath}/">
                <img src="${pageContext.request.contextPath}\resources\images\logo.png" alt="Logo">
            </a>
        </div>
        <nav class="nav">
        </nav>
    </header>

    <h1>Capture and Analyze Photo from Webcam</h1>
    <div class="webcam-container">
        <button id="prevPage" class="nav-icon">
            <a href="${pageContext.request.contextPath}/select">
            <img src="${pageContext.request.contextPath}\resources\images\icon_left.png" alt="left">
            </a>
        </button>
        <video id="video" width="480" height="360" autoplay></video>
        <button id="nextPage" class="nav-icon">
            <a href="${pageContext.request.contextPath}/resultf">
            <img src="${pageContext.request.contextPath}\resources\images\icon_right.png" alt="right">
            </a>
        </button>
    </div>
    <div class="button-container">
        <button id="capture-btn">Capture Photo</button>
        <button id="upload-btn">Upload</button>
    </div>
    <div id="capturedImagesContainer">
        <canvas id="canvas" width="320" height="240" style="display:none;"></canvas>
        <img id="captured-image" src="" alt="Captured Image" style="display:none;">
    </div>



    <script>
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
                var video = document.getElementById('video');
                video.srcObject = stream;
                video.play();
            })
            .catch(function(err) {
                console.log("An error occurred: " + err);
            });

        var canvas = document.getElementById('canvas');
        var context = canvas.getContext('2d');
        var video = document.getElementById('video');
        var captureBtn = document.getElementById('capture-btn');
        var uploadBtn = document.getElementById('upload-btn');
        var capturedImage = document.getElementById('captured-image');

        captureBtn.addEventListener('click', function() {
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            capturedImage.src = canvas.toDataURL('image/png');
            capturedImage.style.display = 'block';
        });

        uploadBtn.addEventListener('click', function() {
            canvas.toBlob(function(blob) {
                var formData = new FormData();
                formData.append('file', blob, 'snapshot.png');

                // Ajax 요청
                $.ajax({
                    url: '/helloSpringMVC/upload',
                    type: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false,
                    success: function(response) {
                        console.log('Image uploaded successfully:', response);
                        alert("업로드가 완료되었습니다.")
                    },
                    error: function(xhr, status, error) {
                        console.error('Error sending image:', error);
                        // 에러 시 동작할 내용 추가
                    }
                });
            });
        });
    </script>
</body>
</html>
