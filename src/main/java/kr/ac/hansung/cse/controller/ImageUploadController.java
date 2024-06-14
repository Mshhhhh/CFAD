package kr.ac.hansung.cse.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

@Controller
public class ImageUploadController {

    @PostMapping("/upload")
    public ResponseEntity<String> handleImageUpload(@RequestParam("file") MultipartFile file) {
        if (file.isEmpty()) {
            return new ResponseEntity<>("No file received", HttpStatus.BAD_REQUEST);
        }

        try {
            // 받은 파일을 저장할 경로 설정
            String uploadDir = "C://dev/workspace/Homework1/src/main/webapp/resources/uploads";
            File uploadPath = new File(uploadDir);
            if (!uploadPath.exists()) {
                uploadPath.mkdirs();
            }

            // 파일 이름 설정
            String fileName = "uploaded_image.png";
            File uploadedFile = new File(uploadPath, fileName);

            // 파일 저장
            try (OutputStream outputStream = new FileOutputStream(uploadedFile)) {
                outputStream.write(file.getBytes());
            }

            // 성공 메시지 반환
            return new ResponseEntity<>("File uploaded successfully", HttpStatus.OK);
        } catch (IOException e) {
            e.printStackTrace();
            return new ResponseEntity<>("Failed to upload file", HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
    @PostMapping("/facial")
    public static void runPythonScript() throws IOException {
        ProcessBuilder pb = new ProcessBuilder("python", "C://dev/workspace/Homework1/src/main/webapp/resources/FER_API/app.py");
        Process process = pb.start();


        try {
            int exitCode = process.waitFor();
            System.out.println("Exited with error code " + exitCode);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

