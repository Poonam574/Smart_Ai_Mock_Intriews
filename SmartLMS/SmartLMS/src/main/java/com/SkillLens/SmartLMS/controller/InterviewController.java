package com.SkillLens.SmartLMS.controller;
import com.SkillLens.SmartLMS.Service.EmailService;
import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/interview")
public class InterviewController {

    @Autowired
    private EmailService emailService;

    @GetMapping("/send")
    public String sendLink() {

        emailService.sendInterviewLink("mybigdrea2112@gmail.com");

        return "Interview email sent";
    }
}