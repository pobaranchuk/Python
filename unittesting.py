#Assert Methods 
import unittest
import entertainment
import alerts

# Assert Methods III: Exception and Warning Methods

class SystemAlertTests(unittest.TestCase):
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)
    #The assertRaises() method takes an exception type as its first argument, a function reference as its second, and an arbitrary number of arguments as the rest. 
    # It calls the function and checks if an exception is raised as a result. The test passes if an exception is raised, is an error if another exception is raised,
    # or fails if no exception is raised. This method can be used with custom exceptions as well!



  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)
    #The assertWarns() method takes a warning type as its first argument, a function reference as its second, and an arbitrary number of arguments for the rest.
    # It calls the function and checks that the warning occurs. The test passes if a warning is triggered and fails if it isn’t.


class EntertainmentSystemTests(unittest.TestCase):

    # The assertEqual() method takes two values as arguments and checks that they are equal.
    #  If they are not, the test fails.

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)
    #The assertIn() method takes two arguments.It checks that the first argument is found in the second argument, which should be a container.
    # If it is not found in the container, the test fails.


  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)
    #The assertTrue() method takes a single argument and checks that the argument evaluates to True. 
    # If it does not evaluate to True, the test fails.

  
  def test_maximum_display_brightness(self):
    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)
    #The assertAlmostEqual() method takes two arguments and checks that their difference, when rounded to 7 decimal places, is 0.
    #  In other words, if they are almost equal. If the value is close enough to equality, the test will fail.


  def test_device_temperature(self):
    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)
    #The assertLess() method takes two arguments and checks that the first argument is less than the second one. 
    # If it is not, the test will fail.

#Parameterizing Tests:

#By using subTest, each iteration of our loop is treated as an individual test.
#  Python will run the code inside of the context manager on each iteration,
#  and if one fails, it will return the failure as a separate test case failure.
class EntertainmentSystemTests_subTest(unittest.TestCase):

  def test_movie_license(self):
    daily_movies = entertainment.get_daily_movie_list()
    licensed_movies = entertainment.get_licensed_movies()

    # Write your code below:
    for movie in daily_movies:
      print(movie)
      with self.subTest(movie):
        self.assertIn(movie, licensed_movies)

#Test Fixtures

#A test fixture is a mechanism for ensuring proper test setup (putting tests into a known state) and test teardown (restoring the state prior to the test running).
#  Test fixtures guarantee that our tests are running in predictable conditions, and thus the results are reliable.



unittest.main()