import 'package:flutter/material.dart';
import 'package:fitness_app_live/constants/color.dart';
import 'package:fitness_app_live/screens/profile_page/profile_page.dart';
import 'package:fitness_app_live/screens/home_screen/notifications.dart';
import 'package:fitness_app_live/screens/home_screen/home_screen.dart';
import 'package:fitness_app_live/screens/home_screen/workout_progress.dart';

class HomepageNavbar extends StatefulWidget {
  const HomepageNavbar({Key? key}) : super(key: key);

  @override
  State<HomepageNavbar> createState() => _HomepageNavbarState();
}

class _HomepageNavbarState extends State<HomepageNavbar> {
  int _selectedIndex = 0;
  static List<Widget> _widgetOptions = <Widget>[
    HomePage(),
    workoutProgress(),
    NotificationPage(),
    ProfilePage(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        backgroundColor: Colors.black,
        body: Stack(
          children: [
            _widgetOptions.elementAt(_selectedIndex),
            Positioned(
              bottom: 0,
              left: MediaQuery.of(context).size.width / 2 - 28, // Adjust the position of the icon horizontally
              child: GestureDetector(
                onTap: () {
                  // Add functionality for the AI assistant here
                },
                child: Container(
                  width: 56,
                  height: 56,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: Colors.blue,
                  ),
                  child: Image.asset('assets/images/ai.png'), // Add the image asset here
                ),
              ),
            ),
          ],
        ),
        bottomNavigationBar: Theme(
          data: Theme.of(context).copyWith(
            canvasColor: Colors.black,
          ),
          child: BottomNavigationBar(
            items: const <BottomNavigationBarItem>[
              BottomNavigationBarItem(
                icon: Icon(Icons.home),
                label: 'Home',
              ),
              BottomNavigationBarItem(
                icon: Icon(Icons.poll),
                label: 'Progress',
              ),
              BottomNavigationBarItem(
                icon: Icon(Icons.notifications_active_sharp),
                label: 'Notifications',
              ),
              BottomNavigationBarItem(
                icon: Icon(Icons.person),
                label: 'Profile',
              ),
            ],
            currentIndex: _selectedIndex,
            selectedItemColor: PrimaryColor,
            unselectedItemColor: Colors.grey,
            onTap: _onItemTapped,
          ),
        ),
      ),
    );
  }
}

// void main() {
//   runApp(MaterialApp(
//     home: HomepageNavbar(),
//   ));
// }
