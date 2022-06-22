from django.test import TestCase, LiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from food.models import BlogPost, Comment, UserDataModel
from model_bakery import baker
from selenium import webdriver
import datetime
import time



class LoginFormTest(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000/log/form/')

		# Get element of user email field
		self.user_name = self.driver.find_element_by_id('id_email')
		# Get element of password field
		self.user_password = self.driver.find_element_by_id('id_pwd')
		# Get element of login button
		self.login_submit = self.driver.find_element_by_id("id_log_btn")

	def test_login_form_email_field(self):
		time.sleep(1)
		# Fill the email field 
		self.user_name.send_keys("prakhardw1996@gmail.com")

		time.sleep(1)
		# Fill the password field
		self.user_password.send_keys("Myadmin123")

		time.sleep(1)
		self.login_submit.send_keys(Keys.RETURN)

		time.sleep(2)
		dashboard_template_title = self.driver.title
		self.assertNotEqual(dashboard_template_title, 'Ogani | Template')
		self.assertFalse("prakhardwi1996@gmail.com" in self.driver.page_source)

	def test_login_form_password_field_minimum_characters(self):
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")

		time.sleep(1)
		# Fill the password field
		self.user_password.send_keys("M123")

		time.sleep(1)
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)
		dashboard_template_title = self.driver.title
		self.assertNotEqual(dashboard_template_title, 'Ogani | Template')
		self.assertTrue("prakhardwi1996@gmail.com" in self.driver.page_source)

	def test_login_form_password_field_maximum_characters(self):
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")

		time.sleep(1)
		# Fill the password field
		self.user_password.send_keys("M123admin@14uhvbfui")

		time.sleep(1)
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)
		dashboard_template_title = self.driver.title
		self.assertNotEqual(dashboard_template_title, 'Ogani | Template')
		self.assertTrue("prakhardwi1996@gmail.com" in self.driver.page_source)

	def test_login_form(self):
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")

		time.sleep(1)
		# Fill the password field
		self.user_password.send_keys("Myadmin123")

		time.sleep(1)
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)
		dashboard_template_title = self.driver.title
		self.assertEqual(dashboard_template_title, 'Ogani | Template')
		self.assertTrue("prakhardwi1996@gmail.com" in self.driver.page_source)
		

	def tearDown(self):
		self.driver.close()


class RegisterFormTestCase(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000/reg/form/')

		# Get element of full name field
		self.full_name = self.driver.find_element_by_id('id_full_name')
		# Get element of user name field
		self.user_name = self.driver.find_element_by_id('id_username')
		# Get element of user email field 
		self.user_email = self.driver.find_element_by_id('id_email')
		# Get element of user address field
		self.user_address = self.driver.find_element_by_id('id_addr')
		# Get element of user mobile number field
		self.user_mobile_number = self.driver.find_element_by_id('id_mobile_no')
		# Get element of user district name field
		self.user_district_name = self.driver.find_element_by_id("id_district")
		# Get element of state name field
		self.user_state_name = self.driver.find_element_by_id("id_state")
		# Get element of country name field
		self.user_country_name = self.driver.find_element_by_id("id_country")
		# Get element of user password field
		self.user_password = self.driver.find_element_by_id("id_password1")
		# Get element of user confirm password field
		self.user_confirm_password = self.driver.find_element_by_id("id_password2")
		# Get element of register form button
		self.register_form_submit_button = self.driver.find_element_by_id("reg_btn_id")

	def test_register_form_required_fields(self):
		self.full_name.send_keys("")
		self.user_name.send_keys("")
		self.user_email.send_keys("")
		self.user_address.send_keys("")
		self.user_mobile_number.send_keys("")
		self.user_district_name.send_keys("")
		self.user_state_name.send_keys("")
		self.user_country_name.send_keys("")
		self.user_password.send_keys("")
		self.user_confirm_password.send_keys("")
		time.sleep(2)
		self.register_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(5)
		self.assertEqual(self.driver.title, 'Registration Form')


	def test_register_form_username_field(self):
		self.full_name.send_keys("Sunil Dwivedi")
		self.user_name.send_keys("PRAKDWI112")
		self.user_email.send_keys("sunildwi1996@gmail.com")
		self.user_address.send_keys("F-38 Sudama Nagar, Ratlam [M.P]")
		self.user_mobile_number.send_keys("9074606891")
		self.user_district_name.send_keys("Ujjain")
		self.user_state_name.send_keys("Maharashtra")
		self.user_country_name.send_keys("India")
		self.user_password.send_keys("Myadmin123")
		self.user_confirm_password.send_keys("Myadmin123")
		time.sleep(2)
		self.register_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(5)
		self.assertEqual(self.driver.title, 'Registration Form')

	def test_register_form_mobile_number_field(self):
		self.full_name.send_keys("Sunil Dwivedi")
		self.user_name.send_keys("prakdwi113")
		self.user_email.send_keys("sunildwi1996@gmail.com")
		self.user_address.send_keys("F-38 Sudama Nagar, Ratlam [M.P]")
		self.user_mobile_number.send_keys("9006891")
		self.user_district_name.send_keys("Ujjain")
		self.user_state_name.send_keys("Maharashtra")
		self.user_country_name.send_keys("India")
		self.user_password.send_keys("Myadmin123")
		self.user_confirm_password.send_keys("Myadmin123")
		time.sleep(2)
		self.register_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(5)
		self.assertEqual(self.driver.title, 'Registration Form')


	def test_register_form_password_field(self):
		self.full_name.send_keys("Sunil Dwivedi")
		self.user_name.send_keys("prakdwi113")
		self.user_email.send_keys("sunildwi1996@gmail.com")
		self.user_address.send_keys("F-38 Sudama Nagar, Ratlam [M.P]")
		self.user_mobile_number.send_keys("6260336626")
		self.user_district_name.send_keys("Ujjain")
		self.user_state_name.send_keys("Maharashtra")
		self.user_country_name.send_keys("India")
		self.user_password.send_keys("Myadmon123")
		self.user_confirm_password.send_keys("Myadmin123")
		time.sleep(2)
		self.register_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(5)
		self.assertEqual(self.driver.title, 'Registration Form')

	def test_register_form_email_field(self):
		self.full_name.send_keys("Prakhar Dwivedi")
		self.user_name.send_keys("prak123dwi")
		self.user_email.send_keys("prakhardwi1996@gmail.com")
		self.user_address.send_keys("F-38 Dindayal Nagar, Ratlam [M.P]")
		self.user_mobile_number.send_keys("6260336626")
		self.user_district_name.send_keys("Ratlam")
		self.user_state_name.send_keys("Madhya Pradesh")
		self.user_country_name.send_keys("India")
		self.user_password.send_keys("Myadmin123")
		self.user_confirm_password.send_keys("Myadmin123")
		time.sleep(2)
		self.register_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(5)
		self.assertEqual(self.driver.title, 'Registration Form')

	def test_register_form_successfully(self):
		self.full_name.send_keys("Pratik Dwivedi")
		self.user_name.send_keys("pratikl123i")
		self.user_email.send_keys("pratikdwi1996@gmail.com")
		self.user_address.send_keys("F-38 Sudama Nagar, Ratlam [M.P]")
		self.user_mobile_number.send_keys("9389228844")
		self.user_district_name.send_keys("Ujjain")
		self.user_state_name.send_keys("Bihar")
		self.user_country_name.send_keys("India")
		self.user_password.send_keys("Myadmin123")
		self.user_confirm_password.send_keys("Myadmin123")
		time.sleep(2)
		self.register_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(2)
		self.assertNotEqual(self.driver.title, 'Registration Form')

	def tearDown(self):
		self.driver.close()


class ProductLikesTestCase(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000')
		# Get element of login button on main dashboard
		self.login_button_on_dashboard = self.driver.find_element_by_id('id-for-login')
		
		self.login_button_on_dashboard.click()
		# Get element of user email field
		self.user_name = self.driver.find_element_by_id("id_email")
		# Get element of password field
		self.user_password = self.driver.find_element_by_id("id_pwd")
		# Get element of login button
		self.login_submit = self.driver.find_element_by_id("id_log_btn")
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")
		# Fill the password field
		self.user_password.send_keys("Myadmin123")
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)
		

	def test_product_as_liked(self):
		self.favourite_button = self.driver.find_element_by_xpath('//*[@id="2-like-id"]')
		time.sleep(3)
		self.driver.execute_script("arguments[0].click();", self.favourite_button)
		time.sleep(3)
		self.food_liked_modal_ok_button = self.driver.find_element_by_id("dis-modal")
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue("prakhardwi1996@gmail.com" in self.driver.page_source)
		# self.assertTrue("Added as Liked" in self.driver.page_source)
		self.food_liked_modal_ok_button.click()

	def test_product_as_already_liked(self):
		self.favourite_button = self.driver.find_element_by_xpath('//*[@id="2-like-id"]')
		time.sleep(3)
		self.driver.execute_script("arguments[0].click();", self.favourite_button)
		time.sleep(3)
		self.food_liked_modal_ok_button = self.driver.find_element_by_id("dis-modal")
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue("prakhardwi1996@gmail.com" in self.driver.page_source)
		# self.assertTrue("You have already Liked this fruit" in self.driver.page_source)
		self.food_liked_modal_ok_button.click()


	def tearDown(self):
		self.driver.quit()


class FoodCartTestCase(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000')
		# Get element of login button on main dashboard
		self.login_button_on_dashboard = self.driver.find_element_by_id('id-for-login')
		self.login_button_on_dashboard.click()
		# Get element of user email field
		self.user_name = self.driver.find_element_by_id("id_email")
		# Get element of password field
		self.user_password = self.driver.find_element_by_id("id_pwd")
		# Get element of login button
		self.login_submit = self.driver.find_element_by_id("id_log_btn")
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")
		# Fill the password field
		self.user_password.send_keys("Myadmin123")
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)


	def test_product_as_cart_feature(self):
		self.cart_button = self.driver.find_element_by_xpath('//*[@id="2-cart-id"]')
		time.sleep(3)
		self.driver.execute_script("arguments[0].click();", self.cart_button)
		time.sleep(3)
		self.food_liked_modal_ok_button = self.driver.find_element_by_id("dis-modal")
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue("prakhardwi1996@gmail.com" in self.driver.page_source)
		self.food_liked_modal_ok_button.click()
		time.sleep(2)

	def test_product_as_included_in_cart(self):
		self.cart_button = self.driver.find_element_by_xpath('//*[@id="2-cart-id"]')
		time.sleep(3)
		self.driver.execute_script("arguments[0].click();", self.cart_button)
		time.sleep(3)
		self.food_liked_modal_ok_button = self.driver.find_element_by_id("dis-modal")
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue("prakhardwi1996@gmail.com" in self.driver.page_source)
		self.food_liked_modal_ok_button.click()
		time.sleep(2)

	def tearDown(self):
		self.driver.quit()


class AddProductReviewTestCase(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000')
		# Get element of login button on main dashboard
		self.login_button_on_dashboard = self.driver.find_element_by_id('id-for-login')
		
		self.login_button_on_dashboard.click()
		# Get element of user email field
		self.user_name = self.driver.find_element_by_id("id_email")
		# Get element of password field
		self.user_password = self.driver.find_element_by_id("id_pwd")
		# Get element of login button
		self.login_submit = self.driver.find_element_by_id("id_log_btn")
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")
		# Fill the password field
		self.user_password.send_keys("Myadmin123")
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)

	def test_product_review_form_feature(self):
		time.sleep(3)
		self.product_link = self.driver.find_element_by_id('food-7')
		time.sleep(3)
		self.driver.execute_script("arguments[0].click();", self.product_link)
		time.sleep(3)
		self.assertEqual(self.driver.title, 'Ogani | Template')
		# Get Product Review element Link
		self.product_review_link_element = self.driver.find_element_by_id('food-review-7')
		self.driver.execute_script("arguments[0].click();", self.product_review_link_element)
		time.sleep(3)
		# Get Product Review Form field element
		self.product_review_field = self.driver.find_element_by_id('review-form-control')
		# Get Product Review Form submit button element
		self.product_review_form_submit_button = self.driver.find_element_by_id('review-form-submit-btn-id')
		# Fill food review form field
		self.product_review_field.send_keys("This is very sweet Fruits")
		# self.assertTrue("This is very sweet Fruits" in self.driver.page_source)
		time.sleep(2)
		self.product_review_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(2)

	def tearDown(self):
		self.driver.quit()


class BlogCategoryTestCase(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000')
		# Get element of login button on main dashboard
		self.login_button_on_dashboard = self.driver.find_element_by_id('id-for-login')
		self.login_button_on_dashboard.click()
		# Get element of user email field
		self.user_name = self.driver.find_element_by_id("id_email")
		# Get element of password field
		self.user_password = self.driver.find_element_by_id("id_pwd")
		# Get element of login button
		self.login_submit = self.driver.find_element_by_id("id_log_btn")
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")
		# Fill the password field
		self.user_password.send_keys("Myadmin123")
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)

	def test_blog_category_search(self):
		self.blog_button__for_user = self.driver.find_element_by_id('blog')
		self.blog_button__for_user.click()
		time.sleep(3)
		self.blog_category_link_element = self.driver.find_element_by_xpath('//*[@id="food"]/a')
		self.driver.execute_script("arguments[0].click();", self.blog_category_link_element)
		time.sleep(3)
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue("Food" in self.driver.page_source)
		self.assertTrue("Can Breakfast Help You Lose Weight?" in self.driver.page_source)
		self.assertTrue("Can Breakfast is necessary?" in self.driver.page_source)
		self.assertTrue("Is breakfast really the most important meal of the day?" in self.driver.page_source)
		time.sleep(4)


	def tearDown(self):
		self.driver.quit()


class BlogSearchByTagTestCase(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000')
		# Get element of login button on main dashboard
		self.login_button_on_dashboard = self.driver.find_element_by_id('id-for-login')
		self.login_button_on_dashboard.click()
		# Get element of user email field
		self.user_name = self.driver.find_element_by_id("id_email")
		# Get element of password field
		self.user_password = self.driver.find_element_by_id("id_pwd")
		# Get element of login button
		self.login_submit = self.driver.find_element_by_id("id_log_btn")
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")
		# Fill the password field
		self.user_password.send_keys("Myadmin123")
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)

	def test_blog_search_by_tag(self):
		self.blog_button_element_for_user = self.driver.find_element_by_id('blog')
		self.blog_button_element_for_user.click()
		time.sleep(3)
		self.blog_search_tag_element_for_user = self.driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div/div[1]/div/div[4]/div/a[2]')
		self.driver.execute_script("arguments[0].click();", self.blog_search_tag_element_for_user)
		time.sleep(3)
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue("Blogs" in self.driver.page_source)
		self.assertTrue("Food" in self.driver.page_source)
		self.assertTrue("Breakfast" in self.driver.page_source)
		self.assertTrue("Can Breakfast Help You Lose Weight?" in self.driver.page_source)
		time.sleep(4)

	def tearDown(self):
		self.driver.quit()


class BlogSearchBarTestCase(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000')
		# Get element of login button on main dashboard
		self.login_button_on_dashboard = self.driver.find_element_by_id('id-for-login')
		self.login_button_on_dashboard.click()
		# Get element of user email field
		self.user_name = self.driver.find_element_by_id("id_email")
		# Get element of password field
		self.user_password = self.driver.find_element_by_id("id_pwd")
		# Get element of login button
		self.login_submit = self.driver.find_element_by_id("id_log_btn")
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")
		# Fill the password field
		self.user_password.send_keys("Myadmin123")
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)

	def test_blog_search_bar(self):
		self.blog_button_element_for_user = self.driver.find_element_by_id('blog')
		self.blog_button_element_for_user.click()
		time.sleep(3)
		self.blog_search_bar_for_user = self.driver.find_element_by_id('blog-search-bar')
		self.blog_search_bar_for_user.send_keys('Can Breakfast Help You Lose Weight?')
		time.sleep(3)
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue("Blogs" in self.driver.page_source)
		self.assertTrue("Food" in self.driver.page_source)
		self.assertTrue("Can Breakfast Help You Lose Weight?" in self.driver.page_source)
		time.sleep(4)

	def tearDown(self):
		self.driver.quit()


class BlogCommentTestCase(LiveServerTestCase):

	def create_blog_object(self):
		blog_object = BlogPost.objects.create(blog_title = 'Can Breakfast Help You Lose Weight?',
											 blog_category = "Food",
											 blog_body = "This is blog body",
											 blog_post_date = datetime.date.today())
		return blog_object


	def create_comment_object(self):
		self.user = baker.make(UserDataModel, full_name = 'Pulkit Soni')
		blog_object = self.create_blog_object()
		comment_object = Comment.objects.create(post = blog_object,
												name = self.user,
												content = 'My first comment is this',
												publish = datetime.date.today())
		return comment_object

	def setUp(self):
		self.driver = webdriver.Chrome('C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe')
		# Choose your URL to visit
		self.driver.get('http://127.0.0.1:8000')
		# Get element of login button on main dashboard
		self.login_button_on_dashboard = self.driver.find_element_by_id('id-for-login')
		self.login_button_on_dashboard.click()
		# Get element of user email field
		self.user_name = self.driver.find_element_by_id("id_email")
		# Get element of password field
		self.user_password = self.driver.find_element_by_id("id_pwd")
		# Get element of login button
		self.login_submit = self.driver.find_element_by_id("id_log_btn")
		# Fill the email field 
		self.user_name.send_keys("prakhardwi1996@gmail.com")
		# Fill the password field
		self.user_password.send_keys("Myadmin123")
		self.login_submit.send_keys(Keys.RETURN)
		time.sleep(2)
		self.comment_object = self.create_comment_object()
		self.blog_object = self.create_blog_object()


	def test_blog_comment_form_submit_successfully(self):
		self.blog_button_element_for_user = self.driver.find_element_by_id('blog')
		self.blog_button_element_for_user.click()
		time.sleep(3)
		self.blog_article_to_read = self.driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div/div[2]/div/div[1]/div/div[2]/h5/a')
		self.driver.execute_script("arguments[0].click();", self.blog_article_to_read)
		time.sleep(3)
		self.blog_article_comment_form_link = self.driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div/div[2]/div[3]/div')
		self.driver.execute_script("arguments[0].click();", self.blog_article_comment_form_link)
		time.sleep(3)
		self.blog_article_comment_form_content = self.driver.find_element_by_id('comment-content-id')
		self.blog_article_comment_form_content.send_keys("My first comment is this")
		self.blog_article_comment_form_submit_button = self.driver.find_element_by_id('comment-form-submit-id')
		self.blog_article_comment_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(3)
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue(self.comment_object.content in self.driver.page_source)
		self.assertTrue(self.blog_object.blog_title in self.driver.page_source)

	def test_blog_comment_required_field(self):
		self.blog_button_element_for_user = self.driver.find_element_by_id('blog')
		self.blog_button_element_for_user.click()
		time.sleep(3)
		self.blog_article_to_read = self.driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div/div[2]/div/div[1]/div/div[2]/h5/a')
		self.driver.execute_script("arguments[0].click();", self.blog_article_to_read)
		time.sleep(3)
		self.blog_article_comment_form_link = self.driver.find_element_by_xpath('/html/body/div[3]/section[2]/div/div/div[2]/div[3]/div')
		self.driver.execute_script("arguments[0].click();", self.blog_article_comment_form_link)
		time.sleep(3)
		self.blog_article_comment_form_content = self.driver.find_element_by_id('comment-content-id')
		self.blog_article_comment_form_content.send_keys("")
		self.blog_article_comment_form_submit_button = self.driver.find_element_by_id('comment-form-submit-id')
		self.blog_article_comment_form_submit_button.send_keys(Keys.RETURN)
		time.sleep(3)
		self.comment_last_object = Comment.objects.last()
		self.assertEqual(self.driver.title, 'Ogani | Template')
		self.assertTrue(self.comment_object.content in self.driver.page_source)
		self.assertTrue(self.blog_object.blog_title in self.driver.page_source)


	def tearDown(self):
		self.driver.quit()











































