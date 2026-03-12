package com.SkillLens.SmartLMS.Service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class EmailService {

    @Autowired
    private JavaMailSender mailSender;

    public void sendInterviewLink(String candidateEmail) {

        String interviewLink = "http://127.0.0.1:5000";

        SimpleMailMessage message = new SimpleMailMessage();
        message.setTo(candidateEmail);   // FIXED
        message.setSubject("AI Mock Interview Link");
        message.setText(
                "Hello Candidate,\n\n" +
                        "Click the link below to start your interview:\n\n" +
                        interviewLink +
                        "\n\nBest Regards\nSmartLMS Team"
        );

        mailSender.send(message);
    }
}