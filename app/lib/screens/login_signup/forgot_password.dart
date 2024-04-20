import 'package:fitness_app_live/config.dart';
import 'package:fitness_app_live/constants/color.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class ForgotPassword extends StatelessWidget {
  const ForgotPassword({super.key});

  Future<void> resetPassword(String email, String newPassword, BuildContext context) async {
    final response = await http.post(
      Uri.parse(forgotPasswordURL),
      body: {'email': email, 'password': newPassword},
    );

    if (response.statusCode == 200) {
      // Password reset successful
      // Show success message
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Password reset successfully.'),
          duration: Duration(seconds: 2),
        ),
      );
      // Navigate back to the login page
      Navigator.pop(context);
    } else {
      // Password reset failed
      // You can handle the error based on the response status code
      // For example, show an error message to the user
    }
  }

  @override
  Widget build(BuildContext context) {
    var size = MediaQuery.of(context).size;
    TextEditingController emailController = TextEditingController();
    TextEditingController passwordController = TextEditingController();

    return SafeArea(
      child: Scaffold(
        backgroundColor: Colors.black,
        appBar: AppBar(
          leading: IconButton(
            icon: const Icon(Icons.arrow_back_ios),
            onPressed: () {
              Navigator.pop(context);
            },
            color: Colors.white,
          ),
          backgroundColor: Colors.transparent,
        ),
        body: Container(
          width: size.width,
          height: size.height,
          padding: EdgeInsets.only(
            top: size.height * 0.06,
            left: size.width * 0.03,
            right: size.width * 0.05,
            bottom: size.height * 0.03,
          ),
          child: Column(
            children: [
              Text(
                'Forgot Password?'.toUpperCase(),
                style: TextStyle(
                  color: Colors.white,
                  fontSize: size.width * 0.07,
                  fontWeight: FontWeight.bold,
                ),
                textAlign: TextAlign.left,
              ),
              SizedBox(
                height: size.height * 0.02,
              ),
              Text(
                'Enter your email address below to reset your password',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: size.width * 0.04,
                ),
                textAlign: TextAlign.left,
              ),
              SizedBox(
                height: size.height * 0.05,
              ),
              Padding(
                padding: const EdgeInsets.all(10.0),
                child: TextFormField(
                  controller: emailController,
                  keyboardType: TextInputType.emailAddress,
                  decoration: InputDecoration(
                    hintText: 'Email',
                    hintStyle: TextStyle(
                      color: Colors.grey.shade700,
                      fontSize: size.width * 0.04,
                    ),
                    fillColor: Colors.grey.shade800,
                    enabledBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(10),
                      borderSide: BorderSide(
                        color: Colors.grey.shade800,
                      ),
                    ),
                    focusedBorder: const UnderlineInputBorder(
                      borderSide: BorderSide(
                        color: Colors.white,
                      ),
                    ),
                  ),
                ),
              ),
              Spacer(),
              SizedBox(
                height: size.height * 0.02,
              ),
              Container(
                alignment: Alignment.center,
                child: ElevatedButton(
                  onPressed: () {
                    resetPassword(emailController.text, passwordController.text, context);
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: PrimaryColor,
                    padding: EdgeInsets.symmetric(
                      horizontal: size.width * 0.3,
                      vertical: size.height * 0.02,
                    ),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(50),
                    ),
                  ),
                  child: Text(
                    'Send',
                    style: TextStyle(
                      color: Colors.black,
                      fontSize: size.width * 0.04,
                    ),
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
