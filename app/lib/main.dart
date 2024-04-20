import 'package:fitness_app_live/screens/goal_screen/goal_screen.dart';
import 'package:fitness_app_live/screens/login_signup/login_signup.dart';
import 'package:fitness_app_live/screens/login_signup/forgot_password.dart';
import 'package:fitness_app_live/screens/onboarding_screen/onboarding_screen.dart';
import 'package:fitness_app_live/screens/profile_page/profile_page.dart';
import 'package:fitness_app_live/screens/activity_level_screen/activityLevelScreen.dart';
import 'package:fitness_app_live/screens/home_screen/notifications.dart';
import 'package:fitness_app_live/screens/home_screen/bottom_navigation_bar.dart';
import 'package:fitness_app_live/screens/home_screen/home_screen.dart';
import 'package:fitness_app_live/screens/weight_screen/weight_screen.dart';
import 'package:fitness_app_live/screens/workout_categories.dart';

import 'package:flutter/material.dart';

import 'screens/profile_page/privacy_policy.dart';
import 'screens/profile_page/settings_page.dart';
import 'screens/age_screen/age_screen.dart';
import 'screens/gender_screen/gender_screen.dart';
import 'screens/height_screen/height_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      color: Colors.black,
      routes: {
        '/onboarding': (context) => const OnBoardingScreen(),
        '/gender': (context) => const GenderPage(),
        '/age': (context) => const AgePage(),
        '/height': (context) => const HeightPage(),
        '/weight': (context) => const WeightPage(),
        '/activity': (context) => const ActivityLevelPage(),
        '/goal': (context) => const GoalPage(),
        '/forgotPassword': (context) => const ForgotPassword(),
        '/login': (context) => const SignUp(),
        '/home': (context) => const HomePage(),
        '/notifications': (context) => const NotificationPage(),
        '/workoutCategories': (context) => const WorkoutCategories(),
        '/bottomNavigationBar': (context) => const HomepageNavbar(),
        '/profile': (context) => const ProfilePage(),
        '/privacyPolicy': (context) => PrivacyPolicyPage(),
        '/settings': (context) => const SettingsPage(),
        
      },
      debugShowCheckedModeBanner: false,
      home: const OnBoardingScreen(),
    );
  }
}