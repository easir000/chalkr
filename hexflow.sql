-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 30, 2023 at 06:07 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hexflow`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add blog', 7, 'add_blog'),
(26, 'Can change blog', 7, 'change_blog'),
(27, 'Can delete blog', 7, 'delete_blog'),
(28, 'Can view blog', 7, 'view_blog'),
(29, 'Can add profile', 8, 'add_profile'),
(30, 'Can change profile', 8, 'change_profile'),
(31, 'Can delete profile', 8, 'delete_profile'),
(32, 'Can view profile', 8, 'view_profile'),
(33, 'Can add blog section', 9, 'add_blogsection'),
(34, 'Can change blog section', 9, 'change_blogsection'),
(35, 'Can delete blog section', 9, 'delete_blogsection'),
(36, 'Can view blog section', 9, 'view_blogsection'),
(37, 'Can add assistant', 10, 'add_assistant'),
(38, 'Can change assistant', 10, 'change_assistant'),
(39, 'Can delete assistant', 10, 'delete_assistant'),
(40, 'Can view assistant', 10, 'view_assistant'),
(41, 'Can add web section', 11, 'add_websection'),
(42, 'Can change web section', 11, 'change_websection'),
(43, 'Can delete web section', 11, 'delete_websection'),
(44, 'Can view web section', 11, 'view_websection'),
(45, 'Can add web', 12, 'add_web'),
(46, 'Can change web', 12, 'change_web'),
(47, 'Can delete web', 12, 'delete_web'),
(48, 'Can view web', 12, 'view_web');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$390000$Lk5w1l8w3g6lFrLY94kauG$Y3wiTZQqRycdsbO5pg1JxWofz7GU9dEbx4VaKHEhKLw=', '2023-03-23 08:50:41.455029', 0, 'easir956@gmail.com', 'Easir', 'maruf', 'easir956@gmail.com', 0, 1, '2023-03-06 04:13:52.000000'),
(4, 'pbkdf2_sha256$390000$N4bfNJHICaqYsmPiUjiJlW$ng7B4858vcU90X+aG0KuwpxiCuOn+4gAaTvmS2SSEsA=', '2023-03-25 09:35:36.033112', 1, 'chalkr', 'Allen', 'Lamb', 'chalkrai@hexflow.com.au', 1, 1, '2023-03-06 04:21:40.081192');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user_user_permissions`
--

INSERT INTO `auth_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(12, 1, 12),
(13, 1, 13),
(14, 1, 14),
(15, 1, 15),
(16, 1, 16),
(17, 1, 17),
(18, 1, 18),
(19, 1, 19),
(20, 1, 20),
(21, 1, 21),
(22, 1, 22),
(23, 1, 23),
(24, 1, 24),
(25, 1, 25),
(26, 1, 26),
(27, 1, 27),
(28, 1, 28),
(29, 1, 29),
(30, 1, 30),
(31, 1, 31),
(32, 1, 32),
(33, 1, 33),
(34, 1, 34),
(35, 1, 35),
(36, 1, 36);

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_blog`
--

CREATE TABLE `dashboard_blog` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `blogIdea` varchar(200) DEFAULT NULL,
  `keywords` varchar(300) DEFAULT NULL,
  `audience` varchar(100) DEFAULT NULL,
  `wordCount` varchar(200) DEFAULT NULL,
  `uniqueId` varchar(100) DEFAULT NULL,
  `slug` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `last_updated` datetime(6) DEFAULT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dashboard_blog`
--

INSERT INTO `dashboard_blog` (`id`, `title`, `blogIdea`, `keywords`, `audience`, `wordCount`, `uniqueId`, `slug`, `date_created`, `last_updated`, `profile_id`) VALUES
(38, '2. How Software Companies Can Create Engaging Blog Posts Through Research and Visuals \n', 'How To Write a Good Blog Post:', 'Scannable,Research,Visual Engagement', 'Small business, Software company, lodger company , internet service provider', '546', 'efc2fd624894', '2-how-software-companies-can-create-engaging-blog-posts-through-research-and-visuals-efc2fd624894', '2023-03-20 04:09:54.405105', '2023-03-28 10:05:25.993445', 4),
(42, '6. Writing an Effective Blog Post for a Software Company: How to Make it Scannable and Engaging \n', 'How To Write a Good Blog Post:', 'Scannable,Research,Visual Engagement', 'Small business, Software company, lodger company , internet service provider', NULL, '2a4fb1ea853d', '6-writing-an-effective-blog-post-for-a-software-company-how-to-make-it-scannable-and-engaging-2a4fb1ea853d', '2023-03-22 03:45:18.645103', '2023-03-22 03:45:18.654107', 4),
(43, ' Creating a Visual Engagement Web Assistant Using Django and OpenAI GPT-3.5 API in Python', ' How to Build a Web Assistant Using Django and OpenAI GPT-3.5 API in Python', 'Scannable,Research,Visual Engagement', 'Small business, Software company, lodger company , internet service provider', '278', '42e0896c465b', 'creating-a-visual-engagement-web-assistant-using-django-and-openai-gpt-35-api-in-python-42e0896c465b', '2023-03-23 07:53:42.632594', '2023-03-28 10:05:26.030445', 4),
(44, ' Optimizing Your Blog Posts for Maximum Visual Engagement for Lodger Companies', 'How To Write a Good Blog Post:', 'Scannable,Research,Visual Engagement', 'Small business, Software company, lodger company , internet service provider', '319', '2764c2860d58', 'optimizing-your-blog-posts-for-maximum-visual-engagement-for-lodger-companies-2764c2860d58', '2023-03-23 08:51:02.043217', '2023-03-23 08:53:43.627940', 1);

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_blogsection`
--

CREATE TABLE `dashboard_blogsection` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `body` longtext DEFAULT NULL,
  `wordCount` varchar(200) DEFAULT NULL,
  `uniqueId` varchar(100) DEFAULT NULL,
  `slug` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `last_updated` datetime(6) DEFAULT NULL,
  `blog_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dashboard_blogsection`
--

INSERT INTO `dashboard_blogsection` (`id`, `title`, `body`, `wordCount`, `uniqueId`, `slug`, `date_created`, `last_updated`, `blog_id`) VALUES
(25, '1. How to Create a Scannable and Engaging Blog Post Through Research and Visuals \r\n', 'Creating a scannable and engaging blog post is essential for any software company that wishes to stay on top of the competition. In this blog post, we will guide you through the process of researching and incorporating visuals into your blog posts to make them more interesting and informative. <br><br>Research is the key to creating any successful blog post. You need to do adequate research on the topic you are going to write about, which includes reading up on the latest advancements in the field and keeping up with the industry trends. This will help you create a blog post that is up-to-date and relevant. Additionally, you should also consider the interests of your target audience and tailor your blog post accordingly. <br><br>Once you have researched the topic, it’s time to put your blog post together. To make your blog post scannable and engaging, it should be broken down into short paragraphs and sections, with headings and subheadings. This will make it easier for readers to skim through the post and quickly understand the main points. <br><br>In addition to making your blog post scannable, you should also consider incorporating visuals. Visuals such as images, videos, and diagrams help to break up the text and make the blog post more interesting. They also make it easier for readers to understand complex concepts and provide a visual representation of the topic being discussed. <br><br>Finally, don’t forget to proofread and edit your blog post before publishing. This will help ensure that your blog post is free of errors and is easy to read and understand. <br><br>By following these steps, software companies can create engaging blog posts through research and visuals. Doing so will help them reach a wider audience and gain more exposure for their business.', '293', 'a9d26c150250', '1-how-to-create-a-scannable-and-engaging-blog-post-through-research-and-visuals-a9d26c150250', '2023-03-20 04:13:11.440931', '2023-03-20 04:13:11.445970', 38),
(26, '2. The Benefits of Using Research and Visuals in Your Software Company Blog Posts \r\n', 'Creating engaging blog posts for your software company can be a challenge. However, by incorporating research and visuals into your posts, you can create content that is both informative and visually appealing. Research and visuals can provide your software company blog with a number of benefits, from increasing the scannability of your content to providing visual engagement for your readers.<br><br>When it comes to creating engaging blog posts, research is key. Research provides your readers with credible and accurate information that can help them make informed decisions. It also helps to create a more trustworthy and reliable impression of your software company. Furthermore, research can add credibility to your blog post and make it more appealing to potential customers.<br><br>Incorporating visuals into your software company blog posts can also be beneficial. Visuals such as images, graphics, and videos can make your content more engaging and interesting for your readers. Visuals can also help to break up long blocks of text, making your blog posts more scannable and easier to read. Additionally, visuals can help to draw attention to your blog content and make it more shareable.<br><br>Overall, by incorporating research and visuals into your software company blog posts, you can create content that is both informative and visually appealing. Research and visuals can provide your blog with a number of benefits, from increasing the scannability of your content to providing visual engagement for your readers. By utilizing research and visuals in your blog posts, you can make sure that your content stands out from the competition.', '253', '543f5f8491e0', '2-the-benefits-of-using-research-and-visuals-in-your-software-company-blog-posts-543f5f8491e0', '2023-03-20 04:14:05.872151', '2023-03-20 04:14:05.875242', 38),
(27, '4. How Software Companies Can Benefit From Visual Engagement Web Assistants Built With Django and OpenAI GPT-3.5 API in Python \r\n', '<br>Software companies are constantly looking for ways to improve their customer service and increase their online presence. By creating a visual engagement web assistant using Django and OpenAI GPT-3.5 API in Python, software companies can reap the benefits of a more user-friendly interface and improved customer service. <br><br>For starters, software companies can benefit from the scannable and research nature of visual engagement web assistants. By utilizing Django and OpenAI GPT-3.5 API technologies, software companies can create web assistants that are able to quickly scan through customer queries and provide them with the answers they need in a timely manner. This ultimately leads to faster customer service and improved customer satisfaction. <br><br>In addition, software companies can make use of the visual engagement capabilities of web assistants built with Django and OpenAI GPT-3.5 API. By using these technologies, software companies can create web assistants that are able to present information in an engaging, visually appealing way. This allows customers to quickly understand the information presented and make decisions faster.<br><br>Finally, software companies can benefit from the improved security features offered by web assistants built with Django and OpenAI GPT-3.5 API. By using the latest security protocols, software companies can ensure the security of their customer data and protect it from malicious attacks. This ensures that customer data remains safe and secure, resulting in improved customer trust.<br><br>Overall, software companies can benefit greatly from the improved user experience and enhanced security offered by web assistants built with Django and OpenAI GPT-3.5 API. By utilizing these technologies, software companies can create web assistants that are more efficient and easier to use, ultimately leading to improved customer service, better customer satisfaction, and increased online presence.', '278', '2a615b9a50f9', '4-how-software-companies-can-benefit-from-visual-engagement-web-assistants-built-with-django-and-openai-gpt-35-api-in-python-2a615b9a50f9', '2023-03-23 07:57:39.897111', '2023-03-23 07:57:39.901096', 43),
(28, ' 7 Tips for Making Your Blog Posts Visually Engaging for Lodger Companies\r\n', 'When it comes to keeping your lodger company’s blog posts interesting and engaging, visuals are key. But how do you optimize your blog posts to ensure maximum visual engagement? Here are 7 tips for making your blog posts engaging for lodger companies.<br><br>1. Use an Eye-Catching Header Image: A great way to draw readers in is to start with a compelling header image. Choose an image that will grab the reader’s attention and give them a reason to keep reading.<br><br>2. Use Subheadings: Subheadings help break up your text and make it easier to scan. They also help organize your content and make it easier to find the information they’re looking for.<br><br>3. Include High-Quality Images: Including images in your blog post will make it more visually appealing and help illustrate the points you’re making. Make sure you use images that are high-quality and relevant to the content.<br><br>4. Use Videos: Videos are an excellent way to make a post more engaging. They also help break up the text and provide an easy way for readers to absorb information.<br><br>5. Include Infographics: Infographics are a great way to provide readers with a lot of information in a visually pleasing way. They are also great for making complex topics easier to understand.<br><br>6. Incorporate Charts and Graphs: Charts and graphs are also great for breaking up the text and illustrating complex information in an easy to understand format.<br><br>7. Do Your Research: Before you start writing, make sure you do your research. Researching the topic will ensure that you’re providing accurate information and will make it easier to come up with creative visuals that will make your post more engaging.<br><br>By following these tips, you can make sure your blog posts for lodger companies are visually engaging and draw readers in. With an eye-catching header image, subheadings, high-quality images, videos, infographics, charts, and graphs, and plenty of research, you can optimize your blog posts for maximum visual engagement.', '319', 'f951b8b0193f', '7-tips-for-making-your-blog-posts-visually-engaging-for-lodger-companies-f951b8b0193f', '2023-03-23 08:51:39.873146', '2023-03-23 08:51:39.952143', 44);

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_profile`
--

CREATE TABLE `dashboard_profile` (
  `id` bigint(20) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `addressLine1` varchar(100) DEFAULT NULL,
  `addressLine2` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `province` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `postalCode` varchar(100) DEFAULT NULL,
  `profileImage` varchar(100) NOT NULL,
  `uniqueId` varchar(100) DEFAULT NULL,
  `slug` varchar(250) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `last_updated` datetime(6) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `monthlyCount` varchar(100) DEFAULT NULL,
  `subscribed` tinyint(1) NOT NULL,
  `subscriptionReference` varchar(100) DEFAULT NULL,
  `subscriptionType` varchar(100) NOT NULL,
  `bio` longtext NOT NULL,
  `code` varchar(12) NOT NULL,
  `recommended_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dashboard_profile`
--

INSERT INTO `dashboard_profile` (`id`, `first_name`, `last_name`, `addressLine1`, `addressLine2`, `city`, `province`, `country`, `postalCode`, `profileImage`, `uniqueId`, `slug`, `date_created`, `last_updated`, `user_id`, `monthlyCount`, `subscribed`, `subscriptionReference`, `subscriptionType`, `bio`, `code`, `recommended_by_id`) VALUES
(1, 'Easir', 'maruf', 'Dhaka', 'Dhaka', 'Dhaka', 'DHAKA', 'Bangladesh', '1213', 'profile_images/BBB_KcKoFgM.png', '4db758dede1b', 'easir-maruf-easir956gmailcom', '2023-03-23 08:51:39.826153', '2023-03-23 08:51:39.826153', 1, '3424', 0, 'chalkr', 'free', '', 'b8aeb2ee77cc', NULL),
(4, 'Easir', 'maruf', 'Dhaka', 'Dhaka', 'Dhaka', 'DHAKA', 'Bangladesh', '1213', 'profile_images/20211126_184846_CC4yLK4.jpeg', '319c882331f8', 'allen-lamb-chalkraihexflowcomau', '2023-03-28 05:07:54.492877', '2023-03-28 05:07:54.492877', 4, '5908', 0, NULL, 'free', '', '32f7c13f5529', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_web`
--

CREATE TABLE `dashboard_web` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `web` varchar(100) DEFAULT NULL,
  `wordCount` varchar(200) DEFAULT NULL,
  `uniqueId` varchar(100) DEFAULT NULL,
  `slug` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `last_updated` datetime(6) DEFAULT NULL,
  `profile_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dashboard_web`
--

INSERT INTO `dashboard_web` (`id`, `title`, `web`, `wordCount`, `uniqueId`, `slug`, `date_created`, `last_updated`, `profile_id`) VALUES
(1, '\n    \n    predictProba :: [String] -> [Double]\n    predictProba xs = map predictOneProbas xs\n    \n', '    if len (webSections)>0:\r\n', NULL, '6190898f7125', 'predictproba-string-double-predictproba-xs-map-predictoneprobas-xs-6190898f7125', '2023-03-21 10:49:05.771076', '2023-03-21 10:49:05.775062', 4),
(2, '\n\npredictProba :: [String] -> [Float]\npredictProba x = map predictOneProbas x', 'def generateWebSectionDetails(webTopic,sectionTopic,web,prevWeb,profile):', NULL, 'd9941c759980', 'predictproba-string-float-predictproba-x-map-predictoneprobas-x-d9941c759980', '2023-03-21 11:07:01.663006', '2023-03-21 11:07:01.671006', 4),
(3, '\n\npredictProba :: [String] -> [Int]\npredictProba xs = map predictOneProbas xs', 'def generateWebTopicIdeas(web):\r\n  web_topics = []\r\n\r\nconvert into c#', NULL, 'b505642b0db7', 'predictproba-string-int-predictproba-xs-map-predictoneprobas-xs-b505642b0db7', '2023-03-22 04:41:24.860694', '2023-03-22 04:41:24.876691', 4),
(4, '\n\npredictProba :: [String] -> [Int]\npredictProba x = map predictOneProbas x', 'def generateWebTopicIdeas(web):\r\n  web_topics = []\r\n\r\nconvert into c#', NULL, '77014d7fb252', 'predictproba-string-int-predictproba-x-map-predictoneprobas-x-77014d7fb252', '2023-03-22 05:45:59.394760', '2023-03-22 05:45:59.407771', 4),
(5, '\n\npredictProba :: Iterable [String] -> Array Float\npredictProba x = array [predictOneProbas tweet | tweet <- x]', 'vvbvb', NULL, '28a85ce9125b', 'predictproba-iterable-string-array-float-predictproba-x-array-predictoneprobas-tweet-tweet-x-28a85ce9125b', '2023-03-22 06:07:34.545197', '2023-03-22 06:07:34.549161', 4),
(6, '\n\n    predictProba :: [String] -> [Double]\n    predictProba x = map predictOneProbas x', 'class Web(models.Model):\r\n        title  =  models.CharField( max_length=200)\r\n       \r\n   ', NULL, 'cc14bee3bd07', 'predictproba-string-double-predictproba-x-map-predictoneprobas-x-cc14bee3bd07', '2023-03-22 06:18:10.031075', '2023-03-22 06:18:10.035046', 4),
(7, '\n\npredictProba :: [String] -> [Double]\npredictProba xs = map predictOneProbas xs', 'class ProfileImageForm(forms.ModelForm):\r\n\r\n     \r\n\r\nconvert into c++ please \r\n       \r\n   ', NULL, 'bb1540263eea', 'predictproba-string-double-predictproba-xs-map-predictoneprobas-xs-bb1540263eea', '2023-03-22 06:19:24.109957', '2023-03-22 06:19:24.118085', 4),
(8, '\n\npredictProba :: Iterable [String] -> [Array Double]\npredictProba x = np.array [predictOneProbas t | t <- x]', 'def generateBlogTopicIdeas(topic,audience,keywords):\r\n\r\n\r\n\r\nconvert into javascript code', NULL, '0423df2b7779', 'predictproba-iterable-string-array-double-predictproba-x-nparray-predictoneprobas-t-t-x-0423df2b7779', '2023-03-22 06:29:21.325754', '2023-03-22 06:29:21.329758', 4),
(9, '\n\npredictProba :: Iterable [String] -> Array Double\npredictProba x = [predictOneProbas tweet | tweet <- x]', 'path(\'home\', views.home, name=\'dashboard\'),\r\n\r\nconvert into js', NULL, 'f72078bafaa4', 'predictproba-iterable-string-array-double-predictproba-x-predictoneprobas-tweet-tweet-x-f72078bafaa4', '2023-03-23 02:57:40.658349', '2023-03-23 02:57:40.670357', 4);

-- --------------------------------------------------------

--
-- Table structure for table `dashboard_websection`
--

CREATE TABLE `dashboard_websection` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `body` longtext DEFAULT NULL,
  `wordCount` varchar(200) DEFAULT NULL,
  `uniqueId` varchar(100) DEFAULT NULL,
  `slug` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `last_updated` datetime(6) DEFAULT NULL,
  `web_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dashboard_websection`
--

INSERT INTO `dashboard_websection` (`id`, `title`, `body`, `wordCount`, `uniqueId`, `slug`, `date_created`, `last_updated`, `web_id`) VALUES
(1, ' \r\n', '<br>\\prevBlog :<br><br>\\prevBlog :<br><br>\\prevBlog :<br><br>\\prevBlog :<br><br>\\prevBlog :<br><br>\\prevBlog :<br><br>\\prevBlog :<br><br>\\prevBlog :<br><br>\\prevBlog :', '10', '526a6b6e4c1f', '526a6b6e4c1f', '2023-03-21 10:49:53.802177', '2023-03-21 10:49:53.814177', 1),
(2, '/\r\n\r\n// Generate 10 Blog Topic Ideas on the given topic: \r\n\r\n// predictProba :: [String] -> [Double]\r\n// predictProba xs = map predictOneProbas xs\r\n\r\n//  for the related web', '// Generate 10 Blog Topic Ideas on the given topic: \r<br>\r<br>// predictProba :: [String] -> [Double]\r<br>// predictProba xs = map predictOneProbas xs\r<br>\r<br>//  for the', '25', '67de6d333a1d', 'generate-10-blog-topic-ideas-on-the-given-topic-predictproba-string-double-predictproba-xs-map-predictoneprobas-xs-for-the-related-web-67de6d333a1d', '2023-03-21 10:50:50.834406', '2023-03-21 10:50:50.860640', 1),
(3, '/\r\n\r\n// COMMAND ----------\r\n\r\n// MAGIC %md\r\n// MAGIC \r\n// MAGIC ', '// COMMAND ----------\r<br>\r<br>// MAGIC %md\r<br>// MAGIC \r<br>// MAGIC \r<br>// MAGIC \r<br>// MAGIC \r<br>// MAGIC \r<br>// MAGIC \r<br>//', '17', '97a67f9fdbb4', 'command-magic-md-magic-magic-97a67f9fdbb4', '2023-03-21 10:56:39.082833', '2023-03-21 10:56:39.093541', 1),
(4, '/\r\n\r\n// COMMAND ----------\r\n\r\n// MAGIC %md\r\n// MAGIC \r\n// MAGIC ', '// COMMAND ----------\r<br>\r<br>// MAGIC %md\r<br>// MAGIC \r<br>// MAGIC \r<br>// MAGIC \r<br>// MAGIC \r<br>// MAGIC \r<br>// MAGIC \r<br>//', '17', '7e8c93bb5f22', 'command-magic-md-magic-magic-7e8c93bb5f22', '2023-03-21 10:58:40.828377', '2023-03-21 10:58:40.840377', 1),
(5, '\r\n\r\npredictProba :: Iterable[String] -> Array\r\npredictProba x = [predictOneProbas tweet | tweet <- x]', '<br><br>predictProba :: [String] -> [Double]<br>predictProba x = map predictOneProbas x', '10', '54b50606dc32', 'predictproba-iterablestring-array-predictproba-x-predictoneprobas-tweet-tweet-x-54b50606dc32', '2023-03-22 04:41:32.876843', '2023-03-22 04:41:32.885874', 3),
(6, '\r\n\r\npredictProba :: [String] -> Array Double\r\npredictProba x = array [predictOneProbas tweet | tweet <- x]', '<br><br>predictProba :: [String] -> [Double]<br>predictProba x = map predictOneProbas x', '10', '7a0f7c579815', 'predictproba-string-array-double-predictproba-x-array-predictoneprobas-tweet-tweet-x-7a0f7c579815', '2023-03-22 05:46:09.148520', '2023-03-22 05:46:09.160057', 4),
(7, '\r\n\r\npredictProba :: Iterable [String] -> [Float]\r\npredictProba x = map predictOneProbas x', '<br><br>predictProba :: [String] -> [Double]<br>predictProba xs = map predictOneProbas xs', '10', '2cf59fc8b918', 'predictproba-iterable-string-float-predictproba-x-map-predictoneprobas-x-2cf59fc8b918', '2023-03-22 06:07:41.819750', '2023-03-22 06:07:41.828303', 5),
(8, '\r\n\r\n    predictProba :: [String] -> [Float]\r\n    predictProba x = map predictOneProbas x', '<br><br>predictProba :: [String] -> [Double]<br>predictProba xs = map predictOneProbas xs', '10', '48b264294b74', 'predictproba-string-float-predictproba-x-map-predictoneprobas-x-48b264294b74', '2023-03-22 06:18:18.461519', '2023-03-22 06:18:18.469523', 6),
(9, '\r\n\r\n    predictProba :: [String] -> [Float]\r\n    predictProba xs = map predictOneProbas xs', '<br><br>predictProba :: [String] -> [Float]<br>predictProba x = map predictOneProbas x', '10', '21f7025e7bff', 'predictproba-string-float-predictproba-xs-map-predictoneprobas-xs-21f7025e7bff', '2023-03-22 06:29:29.052522', '2023-03-22 06:29:29.063529', 8),
(10, '\r\n\r\npredictProba :: [String] -> [Float]\r\npredictProba x = map predictOneProbas x', '<br><br>predictProba :: Iterable String -> Array Double<br>predictProba x = (map predictOneProbas x)', '12', '5066e7c598a3', 'predictproba-string-float-predictproba-x-map-predictoneprobas-x-5066e7c598a3', '2023-03-22 09:32:49.728483', '2023-03-22 09:32:49.740053', 7),
(11, '\r\n\r\npredictProba :: [String] -> [Double]\r\npredictProba xs = [predictOneProbas x | x <- xs]', '<br><br>predictProba :: [String] -> [Double]<br>predictProba x = map predictOneProbas x', '10', '68cb059ec61c', 'predictproba-string-double-predictproba-xs-predictoneprobas-x-x-xs-68cb059ec61c', '2023-03-23 02:57:48.531317', '2023-03-23 02:57:48.535322', 9);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(3, '2023-03-06 10:04:06.054246', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Subscribed\", \"SubscriptionReference\", \"Bio\", \"Code\", \"Recommended by\"]}}]', 8, 4),
(4, '2023-03-07 04:41:55.477513', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\"]}}]', 8, 4),
(5, '2023-03-07 04:42:07.808314', '4', 'Kevyn Ashley chalkrai@hexflow.com.au ', 2, '[{\"changed\": {\"fields\": [\"Recommended by\"]}}]', 8, 4),
(6, '2023-03-07 04:42:22.822937', '1', 'Easir maruf easir956@gmail.com ', 2, '[]', 8, 4),
(7, '2023-03-07 04:42:28.306425', '1', 'Easir maruf easir956@gmail.com ', 2, '[]', 8, 4),
(8, '2023-03-07 05:47:45.092038', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"UniqueId\"]}}]', 8, 4),
(9, '2023-03-07 05:48:02.688729', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"Recommended by\", \"UniqueId\"]}}]', 8, 4),
(10, '2023-03-07 05:48:14.004586', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"Recommended by\", \"UniqueId\"]}}]', 8, 4),
(11, '2023-03-07 10:12:01.708378', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"UniqueId\", \"Slug\"]}}]', 8, 4),
(12, '2023-03-07 10:12:19.410427', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"UniqueId\", \"Slug\"]}}]', 8, 4),
(13, '2023-03-07 10:12:52.870814', '1', 'easir956@gmail.com', 2, '[{\"changed\": {\"fields\": [\"User permissions\"]}}]', 4, 4),
(14, '2023-03-07 11:04:15.255346', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"Recommended by\", \"UniqueId\", \"Slug\"]}}]', 8, 4),
(15, '2023-03-07 11:06:11.398875', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"UniqueId\", \"Slug\"]}}]', 8, 4),
(16, '2023-03-07 11:06:18.506195', '4', 'Kevyn Ashley chalkrai@hexflow.com.au ', 2, '[{\"changed\": {\"fields\": [\"Recommended by\"]}}]', 8, 4),
(17, '2023-03-09 03:11:18.010901', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"UniqueId\", \"Slug\"]}}]', 8, 4),
(18, '2023-03-09 03:11:35.222650', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"Recommended by\"]}}]', 8, 4),
(19, '2023-03-09 03:11:51.396380', '4', 'Kevyn Ashley chalkrai@hexflow.com.au ', 2, '[{\"changed\": {\"fields\": [\"Code\", \"UniqueId\", \"Slug\"]}}]', 8, 4),
(20, '2023-03-09 03:12:02.767809', '4', 'Kevyn Ashley chalkrai@hexflow.com.au ', 2, '[{\"changed\": {\"fields\": [\"Recommended by\"]}}]', 8, 4),
(21, '2023-03-09 04:14:33.578363', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"UniqueId\", \"Slug\"]}}]', 8, 4),
(22, '2023-03-09 09:27:19.793998', '6', 'cupi@mailinator.com', 3, '', 4, 4),
(23, '2023-03-09 09:27:19.793998', '5', 'povu@mailinator.com', 3, '', 4, 4),
(24, '2023-03-14 04:05:12.330290', '20', '3. Tips for Maximizing the Benefits of an Internet Service Provider for Your Lodging Business \r\n d3764e4f354c', 3, '', 9, 4),
(25, '2023-03-14 04:05:12.333285', '19', '2. Strategies for Finding the Right Internet Service Provider for Your Software Company \r\n 93a80cd940b0', 3, '', 9, 4),
(26, '2023-03-14 04:05:12.335330', '18', '1. How to Ensure Your Internet Service Provider Delivers Quality Service for Your Small Business \r\n 7e49eb9f69ee', 3, '', 9, 4),
(27, '2023-03-14 04:05:12.337476', '17', ' 4. Strategies for Creating Engaging Visuals for Software Companies \r\n 3c906b960000', 3, '', 9, 4),
(28, '2023-03-14 04:05:12.340478', '16', ' 3. Tips for Adding Visual Engagement to Your Blog Posts for Small Businesses \r\n 042631d3b717', 3, '', 9, 4),
(29, '2023-03-14 04:05:12.347663', '15', ' 2. Researching to Increase Visual Engagement on Your Blog Posts for Internet Service Providers \r\n 741afbb08f03', 3, '', 9, 4),
(30, '2023-03-14 04:05:12.350689', '14', ' 1. How to Make Your Blog Posts Scannable for Internet Service Providers \r\n 2f2168da4cc0', 3, '', 9, 4),
(31, '2023-03-14 04:05:12.353689', '13', '1. Utilizing Scannable Content to Create an Attention-Grabbing Blog Post for Internet Service Providers \r\n 81eafba84991', 3, '', 9, 4),
(32, '2023-03-14 04:05:12.355679', '12', '7. How to Leverage Visuals to Increase Engagement and Shares of Your Lodger Company Blog Posts \r\n 3d09f75ceb96', 3, '', 9, 4),
(33, '2023-03-14 04:05:12.358019', '11', '6. Strategies for Creating Engaging Visuals for Your Lodger Company Blog Posts \r\n 21d811466b65', 3, '', 9, 4),
(34, '2023-03-14 04:05:12.360986', '10', '5. Leveraging Visuals to Boost Engagement with Your Lodger Company Blog Posts \r\n d0cce8754f9d', 3, '', 9, 4),
(35, '2023-03-14 04:05:12.362001', '9', '4. How to Make Your Lodger Company Blog Posts Scannable and Engaging \r\n 47ba7e7fd836', 3, '', 9, 4),
(36, '2023-03-14 04:05:12.364000', '8', '3. How to Create Eye-Catching Visuals for Your Lodger Company Blog Posts \r\n 72596acefdaa', 3, '', 9, 4),
(37, '2023-03-14 04:05:12.367256', '7', '2. Research-Backed Tips for Crafting a Visual Engagement Strategy for Your Lodger Company Blog Posts \r\n 7fac6b939e37', 3, '', 9, 4),
(38, '2023-03-14 04:05:12.370254', '6', '1. How to Use Visuals in Your Lodger Company Blog Posts to Increase Engagement \r\n b95a752bc1a8', 3, '', 9, 4),
(39, '2023-03-14 04:05:12.372256', '5', '2. How to Use Research to Improve Visual Engagement on Your Lodger Company Blog Posts \r\n b42a675bde22', 3, '', 9, 4),
(40, '2023-03-14 04:05:12.375233', '4', '1. A Guide to Designing Scannable Content for Your Lodger Company Blog Posts \r\n 9409f6d9d3c6', 3, '', 9, 4),
(41, '2023-03-14 04:05:12.377388', '3', ' 1. How to Write a Scannable Blog Post for Your Internet Service Provider \r\n 4abbc37ef66a', 3, '', 9, 4),
(42, '2023-03-14 04:05:12.380404', '2', '2. How to Create Engaging Visuals for Your Internet Service Provider Blog Posts \r\n 932bbe2b322a', 3, '', 9, 4),
(43, '2023-03-14 04:05:12.382401', '1', '1. How to Make Your Blog Post Scannable and Visual Engaging for Your Internet Service Provider \r\n 48ab84eceeab', 3, '', 9, 4),
(44, '2023-03-14 04:05:22.013574', '28', ' Write an Engaging Blog Post for Internet Service Providers- Essential Tips \n 4c23336fd0e0', 3, '', 7, 4),
(45, '2023-03-14 04:05:22.020645', '27', ' How to Create a Compelling Blog Post for Small Businesses \n 74dbdfec9f77', 3, '', 7, 4),
(46, '2023-03-14 04:05:22.023685', '26', ' Writing a Good Blog Post for Software Companies - Tips and Tricks \n 6e64e64255db', 3, '', 7, 4),
(47, '2023-03-14 04:05:22.026617', '25', ' Writing a Good Blog Post for Lodger Companies - Tips for Visual Engagement 4bcfa91993d1', 3, '', 7, 4),
(48, '2023-03-14 04:05:22.028895', '24', ' 4. How to Add Visual Engagement to Your Blog Posts for Internet Service Providers \n 089e154a2f3f', 3, '', 7, 4),
(49, '2023-03-14 04:05:22.030867', '23', ' 2. How to Research for an Engaging Blog Post for Software Companies \n d0bf528f0ece', 3, '', 7, 4),
(50, '2023-03-14 04:05:22.033885', '22', ' 3. 10 Tips for Writing a Good Blog Post for Lodger Companies \n 0cb1aedc611e', 3, '', 7, 4),
(51, '2023-03-14 04:05:22.035882', '21', ' 1. How to Create a Scannable Blog Post for Small Businesses \n 194d006dc096', 3, '', 7, 4),
(52, '2023-03-14 04:05:22.038028', '20', ' 4. How to Create an Attention-Grabbing Blog Post for Internet Service Providers: Strategies for Research-Backed Content with Visuals \n 644fc461cca6', 3, '', 7, 4),
(53, '2023-03-14 04:05:22.041028', '19', ' 5. Writing a Memorable Blog Post for Small Businesses: Strategies for Scannable Content with Visual Engagement \n ae7d4004bc35', 3, '', 7, 4),
(54, '2023-03-14 04:05:22.043030', '18', ' 6. Crafting a Powerful Blog Post for Software Companies: Using Research, Visuals and Scannable Content \n c5d5fab7de69', 3, '', 7, 4),
(55, '2023-03-14 04:05:22.046224', '17', ' 7. Writing an Engaging Blog Post for Lodging Companies: Tips for Visuals, Scannability and Research-Backed Content 54ae356c4042', 3, '', 7, 4),
(56, '2023-03-14 04:05:22.048226', '16', '3. Creating a Visual Engagement Strategy to Improve Your Lodger Company Blog Posts \n d880d1bf7900', 3, '', 7, 4),
(57, '2023-03-14 04:05:22.050240', '15', '4. How to Use SEO to Make Your Blog Posts Stand Out for Internet Service Providers \n f447a0c95bdd', 3, '', 7, 4),
(58, '2023-03-14 04:05:22.053226', '14', '5. Crafting Compelling Blog Posts for Small Businesses: Tips from the Pros \n 0aefe9ff4968', 3, '', 7, 4),
(59, '2023-03-14 04:05:22.055241', '13', '6. Writing a Good Blog Post for Your Software Company: What You Need to Know \n 4d330d800469', 3, '', 7, 4),
(60, '2023-03-14 04:05:22.058428', '12', '7. The Essential Elements of a Successful Blog Post for Lodger Companies 19d101450d90', 3, '', 7, 4),
(61, '2023-03-14 04:05:22.061426', '11', '4. Proven Strategies for Writing an Engaging Blog Post for Your Internet Service Provider \n 20777b394a12', 3, '', 7, 4),
(62, '2023-03-14 04:05:22.064430', '10', '5. Writing a Good Blog Post: Keys to Success for Small Businesses \n 974041762eea', 3, '', 7, 4),
(63, '2023-03-14 04:05:22.066423', '4', '4. How to Make Your Blog Post Visual Engaging for Your Internet Service Provider \n 7d232b458647', 3, '', 7, 4),
(64, '2023-03-14 04:05:22.068694', '3', '5. Writing Strategies to Make Your Blog Post Stand Out for Small Businesses \n e0e24c805591', 3, '', 7, 4),
(65, '2023-03-14 04:05:22.070670', '2', '6. Tips for Writing a Compelling Blog Post for Software Companies \n fb13658a4da5', 3, '', 7, 4),
(66, '2023-03-14 04:05:22.072685', '1', '7. Crafting an Engaging Blog Post for Your Lodger Company: What You Need To Know 3b8f1228f346', 3, '', 7, 4),
(67, '2023-03-14 07:41:08.361873', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"ProfileImage\"]}}]', 8, 4),
(68, '2023-03-14 07:52:59.346667', '29', '7. The Keys to Writing an Engaging Blog Post for a Lodging Company 3239243fa26a', 2, '[{\"changed\": {\"fields\": [\"UniqueId\"]}}]', 7, 4),
(69, '2023-03-14 07:53:05.378065', '29', '7. The Keys to Writing an Engaging Blog Post for a Lodging Company 13e7fdedbbc8', 2, '[{\"changed\": {\"fields\": [\"UniqueId\"]}}]', 7, 4),
(70, '2023-03-14 07:53:11.449516', '29', '7. The Keys to Writing an Engaging Blog Post for a Lodging Company 4b2ca5740e39', 2, '[{\"changed\": {\"fields\": [\"UniqueId\"]}}]', 7, 4),
(71, '2023-03-14 08:09:23.650738', '1', 'Easir maruf easir956@gmail.com ', 2, '[{\"changed\": {\"fields\": [\"UniqueId\"]}}]', 8, 4),
(72, '2023-03-16 10:03:07.316101', '37', '5. An Overview of the Most Popular Programming Frameworks for Software Engineers \n e9e4b36de228', 3, '', 7, 4),
(73, '2023-03-16 10:03:07.325087', '36', '1. A Comprehensive Comparison of Popular Frameworks for Software Engineers \n cd261dd13e49', 3, '', 7, 4),
(74, '2023-03-16 10:03:07.328086', '35', '2. Top 10 Popular Frameworks Programming for Software Engineers \n fb8e4f657466', 3, '', 7, 4),
(75, '2023-03-16 10:03:07.330083', '34', '5. Crafting an Engaging Blog Post for Software Companies: A Step-by-Step Guide\n 46a59e359d8a', 3, '', 7, 4),
(76, '2023-03-16 10:03:07.333083', '33', '6. Research Strategies for Writing an Effective Blog Post for Small Businesses\n eef79ca6fad0', 3, '', 7, 4),
(77, '2023-03-16 10:03:07.335083', '32', '7. How to Create Visually Engaging Content for Lodging Company Blog Posts e45be0fc2caf', 3, '', 7, 4),
(78, '2023-03-16 10:03:07.338088', '31', '5. Crafting an Engaging and Informative Blog Post for Small Businesses \n a78b469089c9', 3, '', 7, 4),
(79, '2023-03-16 10:03:07.340099', '30', '6. How to Create a Memorable Blog Post for Software Companies \n 4f5512212883', 3, '', 7, 4),
(80, '2023-03-16 10:03:07.342083', '29', '7. The Keys to Writing an Engaging Blog Post for a Lodging Company 4b2ca5740e39', 3, '', 7, 4);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'dashboard', 'assistant'),
(7, 'dashboard', 'blog'),
(9, 'dashboard', 'blogsection'),
(8, 'dashboard', 'profile'),
(12, 'dashboard', 'web'),
(11, 'dashboard', 'websection'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-03-06 04:12:24.508335'),
(2, 'auth', '0001_initial', '2023-03-06 04:12:25.060010'),
(3, 'admin', '0001_initial', '2023-03-06 04:12:25.232841'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-03-06 04:12:25.246072'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-03-06 04:12:25.257797'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-03-06 04:12:25.322001'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-03-06 04:12:25.389377'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-03-06 04:12:25.416700'),
(9, 'auth', '0004_alter_user_username_opts', '2023-03-06 04:12:25.427877'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-03-06 04:12:25.474719'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-03-06 04:12:25.480897'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-03-06 04:12:25.492072'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-03-06 04:12:25.512368'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-03-06 04:12:25.534742'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-03-06 04:12:25.555127'),
(16, 'auth', '0011_update_proxy_permissions', '2023-03-06 04:12:25.566310'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-03-06 04:12:25.586054'),
(18, 'dashboard', '0001_initial', '2023-03-06 04:12:25.865013'),
(19, 'dashboard', '0002_profile_monthlycount_profile_subscribed_and_more', '2023-03-06 04:12:25.949301'),
(20, 'sessions', '0001_initial', '2023-03-06 04:12:25.990339'),
(21, 'dashboard', '0003_profile_bio_profile_code_profile_recommended_by', '2023-03-06 09:30:34.918091'),
(22, 'dashboard', '0004_alter_profile_date_created_and_more', '2023-03-06 09:32:59.050760'),
(23, 'dashboard', '0005_remove_profile_bio_remove_profile_code_and_more', '2023-03-09 07:10:10.049584'),
(24, 'dashboard', '0006_profile_bio_profile_code_profile_recommended_by_and_more', '2023-03-14 08:08:27.422611'),
(25, 'dashboard', '0007_assistant', '2023-03-15 10:23:35.996796'),
(26, 'dashboard', '0008_web_websection_delete_assistant', '2023-03-18 09:28:00.085455'),
(27, 'dashboard', '0009_remove_web_webidea', '2023-03-20 06:46:17.422329'),
(28, 'dashboard', '0010_rename_assistant_web_web', '2023-03-20 06:47:25.051022');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0e9k4jc3s4b3xd6njbtxa5kyaiqwd7fo', '.eJxVjEEOwiAQRe_C2hCgQ4e6dN8zkOkwlaqBpLQr491Nky50-997_60i7VuOe5M1LkldFajL7zYRP6UcID2o3KvmWrZ1mfSh6JM2PdYkr9vp_h1kavmorUiYB9PDZNAG6AVxHhxBcLZDbwx2ljpDjl3qmYMXQONnYAfWI7H6fAHAijbc:1pZP8o:puhmGQsg1E6zDHwtNIOZNAWpJTfpfqrrf6trzfjE1Zk', '2023-03-21 04:41:34.854823'),
('22p4lfy8ozcjjnxuaaodgeb7nyanglwm', '.eJxVjEEOwiAQRe_C2hCgQ4e6dN8zkOkwlaqBpLQr491Nky50-997_60i7VuOe5M1LkldFajL7zYRP6UcID2o3KvmWrZ1mfSh6JM2PdYkr9vp_h1kavmorUiYB9PDZNAG6AVxHhxBcLZDbwx2ljpDjl3qmYMXQONnYAfWI7H6fAHAijbc:1pZ7BT:_qBsrPLLUbfFll4MaiihhHnAaBKL5ccFAcHae1Pm19o', '2023-03-20 09:31:07.039729'),
('3ynspcol563omt4w34pixh7n052tx23t', '.eJxVjM1OwzAQhF9l5VNRUEht12kKvXDnxo2gaGNvYgOykZPAoeq74_wIwV5m99uZubAGp9E200CxcYadmGS3f1mL-p38_DBv6PuQ6-DH6Np8tuTbd8ifgqGPx837r8DiYFNaHCRxUXSkNEpVCC4VmbLCSled2nNVEnJB_EjSCNofZFkUhlei7XipEI1Ipd_UpiJre9uv13P4dHpgpxd2V_vad5PXowseYPHs_A1c6nQBfGEEQDhDcb-CLkTYLdQtNMkD-CRZ9huaByE7g9tC11UijVNMGybMXq8_k5thsA:1pckIp:70kes2S3huGFl8TpDA1TN_hkA_VQdQ4d2j5BySDfwoM', '2023-03-30 09:53:43.709563'),
('4b7escbl5gul10oa22pqx86zcmv1c9rg', '.eJxVjDEOwyAQBP9CHSGMfRxOmd5vQMAdwUkEkrGrKH-PLblIim12ZvctnN_W7LbGi5tJXEUnLr9d8PHJ5QD08OVeZaxlXeYgD0WetMmpEr9up_t3kH3L-5pjQA2ICKpDZQayUUedQKlk0oB9z34PWG1otESRzAgeAygNxEGz-HwBy303qw:1pa6to:eqM2LQ0RsiZHd_f9M0oVbFuBprKapdQ2qkeVWd7cZng', '2023-03-23 03:25:00.920653'),
('4epjimrqkm2c9b6pkul91yrtyn4pzeqg', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pcLSC:M9nc_8yKSJ2ACP04W-aujInG6kdt67g0JvLztRCSK28', '2023-03-29 07:21:44.796285'),
('4hoq0atj2npfr4owoqaxj2ezw3znwnmm', '.eJxVjMsOgjAUBf-la9O0pfTh0j3f0PQ-sKgpCYWV8d-FhIVuz8yct0h5W0vaGi9pInEVVlx-N8j45HoAeuR6nyXOdV0mkIciT9rkMBO_bqf7d1ByK3vNvbbASB0DkQKN2VhPMYAKPeHo0IDboYquc9Yrxx5zVMpjGLVHMOLzBQ_yOIw:1paqgT:546Wxn-EXW-D74B4g1KwkqpPv8_Lfg-1BffU7yRHgdk', '2023-03-25 04:18:17.122329'),
('4iklwtk7pot41c8wdylq999lm89yt6i4', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pevSS:7QMoOX3P5mZqyaZ5ETKlKWAV_1diw5HadUeVH60p7Jg', '2023-04-05 10:12:40.725658'),
('670pwr0nqh1vm8hokq20z1lvtla70264', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pcM9t:sJzISe7TK8Y3FNbzYRr-8oRySND-xpJKc23MYpA6MHA', '2023-03-29 08:06:53.904195'),
('6rihb6miten87o8avak0j1hcj50frozq', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pcKY1:QDhT0WHrc8RLKYqv7x6H8lbu_G30re1JvrVh5BNFl9A', '2023-03-29 06:23:41.838282'),
('8bby3yj4ci3jldsousv2z8jgpshzqwgb', '.eJx1j81KxDAURl8lZK2lk3RSW1BQRHAhCuOuLeU2uZ1Wa1KS1B_Edzed6WJGmazCPd_9TvJNa5h8V08Obd0rmtOEnh3OGpCvqGegXkBvTSSN9rZvojkSLdRFD0bhcLNkjwo6cF3Y5usEGY9bFBISEXOWCFRpBpnMWrFiIkVgHNkFJorjap2kcaxYxpuWpQJA8VD6gU0oKm2pwxve0XrSa2-IJOOA4JDMhOzPct0vPZuxl47mBS11qUeLqpf-yZoGSJ6TYhO-o7cVOb8ixa2ZmgGrP6lPRy7JG4xkmT5q3AEXCK12jg1K3xt90nLv0UKoPrRdWwtfxd1gwP8znhTS6ucXqtaTXw:1perp6:Q1aAUKQftqCXY36Rk9KV3RiH-ktdxVsQeV529bju4vA', '2023-04-05 06:19:48.080988'),
('d1skcknpihsivh8mxyx6m78rhunhts3k', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pfHUz:dU5Fsl3UzXE8wfUEg9z5-bCXjeYFKO-QZLujqPfKlvM', '2023-04-06 09:44:45.624886'),
('ez6ltvewx7pn41sq7ytiq1s7216juw8g', '.eJxVjEEOwiAQRe_C2hCgQ4e6dN8zkOkwlaqBpLQr491Nky50-997_60i7VuOe5M1LkldFajL7zYRP6UcID2o3KvmWrZ1mfSh6JM2PdYkr9vp_h1kavmorUiYB9PDZNAG6AVxHhxBcLZDbwx2ljpDjl3qmYMXQONnYAfWI7H6fAHAijbc:1pZQAY:qD9bejH3SoCRq6Tu_9ViQ0USD7sH-hpUwrvxy2i8iyU', '2023-03-21 05:47:26.731634'),
('fioxfm09xxcqh91j6e7n72qfuw1csdbz', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1peWGK:YFGxdHEASZvyFskl3EMl0x9hxv1_uCePs6ahKWkY-FU', '2023-04-04 07:18:28.499550'),
('g4gx8mnzwc8nxg0z2d3ihglojq69ihru', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pg0JE:Ex78NIkb6jWAZYULfj0F0RlfyCVlO9_y9t1D6MQ0GnA', '2023-04-08 09:35:36.043839'),
('iz574qljsm556tmko3pfm0sseln0iptm', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pbzLU:8eERgpTadboKObRq8Gh3cgti3_OxHJWJRN0MualIGsI', '2023-03-28 07:45:20.890220'),
('j4e627hnqquf0yceqglp024812t53fng', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pcM85:inx1p7Kdf5fmUJo2wDdWH91zMtkV3pr5Il_m7OtW_Xc', '2023-03-29 08:05:01.457992'),
('kd7l1tyryhkjp8xot36zbjzdf140iwln', '.eJxVjEEOwiAQRe_C2hCgQ4e6dN8zkOkwlaqBpLQr491Nky50-997_60i7VuOe5M1LkldFajL7zYRP6UcID2o3KvmWrZ1mfSh6JM2PdYkr9vp_h1kavmorUiYB9PDZNAG6AVxHhxBcLZDbwx2ljpDjl3qmYMXQONnYAfWI7H6fAHAijbc:1pZ7Ci:WNZYhSwuaHTxeGBCmKvpzVGz82iMfbCnSkkbHXfmEHM', '2023-03-20 09:32:24.563394'),
('kjdez285es205d6p75iu3393cmf27qpg', '.eJydVm1P4zgQ_itW70NA6ubSF8qCVJ3Ky3GcQCDRFToBQm48abwkds52Wnqr_e83fklpS8vebb6A4plnHs_zzKTfWs-0NvlzrUE9c9Y6bvVb7dV3E5q-gLAH7CsVUxmnUhjFJ7ENicOpjq8lg-IkxK4B5FTnmN076EO3l2QwSGl_kPS6_QGwwyN6lB5lg053cAi024PuZ-izHnQO-odJwrpHvUnWPRxQynoIOink9JIBtVwgI7ksYU_B3zVos39M7PMLMTkQoxZEG2qgBGEI1ySTimgkxsWUhARipIsd3V4SKhiZgjH22F7IHSjQlRQaAi5ClNSHcOMyFAKCCi-48JWhrAos7JKQhmflEdIc0hcXnoUCnkgJJpfM0ry9uRsvEzAqRMQhYjgkkQ2J3lA9csO9UrKsDGHUUJLh_66MJb4WH6KGS3iLGSPGXuSPov0N_JI63nRb79aeZc-GRFYgKI9PEbAAw6WIUwXYmb3SGmX42DLwaj4xOuMi5Z-SpPfYagdqQ_-n7boJippawbDTRhqvz0aiwfSwkyTJJssVhdb046KqzVpsiAT2vEK4-fchSnPJU9DR00Py9BBZntHTRq1JLVhhK8EM1MLkTlZvATsemLKW0Lwbkm9k84nes0GB379sv88Mch03kq4-3zcYI0dN5rwogm-bHtWF0Q11O1Bxbspi3cdv6qISIuQ3g9cmEdWa47gJ8-sSIGo3d97f5KBqoXePwMX52wRAoWHT6u-uMc_BkVdg04VcYrphwrmnmcEwp5N_1wT87NXwRmhpqp3UM9dJbluIQ_GVzqhOFUctcF29wGIuFdO4rlCgqaKltUmBS7SmU7ARtGYcRAoYoWVm5hRvAWLKBSBsWHhjWfEUMR5aZETsOCnAK2s-A3JRcwZ2GL9Y2pYna9z_JzK580xufW1X_Kop_igQnvwh5y5dryXgm1M3q-QSJVQ0NbbYPUwqzNQhdYxFTkBAxtE_dh2eKTq3y1MTma2i2d2LueQMJShk5VZygOCVX803leEl_8cS_EvWajX7FLeFi7mmr7ysS3ILys0Gdi3AYE9KKcgtNxktCm3pj2aSM2-Ne8XdStjE9LkjNrNIjIwhzQW3srtqZzCpp9NthEI3mzaMBLlBD8w4zO29beuvsHNor5Wc3zEB0AovvlNXfKKo4qBbT17iO0jthvQid2LbdiVZnTZiogXIwZqOK4iW7l1jnvNgnoZeN3aWoaqB2i2ZPb2WdnBkVRdU7arngXsxOX-tCrkExmgPeooXWcNDd7GfIt-PyX1O8WOLZ-5zY8UyzoOI_0X7b9JW5B3AvwXkg032ZzzLcIWgNceLyuNvZ3yMlHiakxvh9s2JVfrjWgN7iwUZKdjVhHONv00Mp8UPkA7j3Rvgv6r3YcM_x-Qi_JS4M1Th1wdXrcl3tmIU6n8IehR_kB_MqXF-t1lwLGXxA86dJN6y_pY2Xxrlf_Wj9fT9X-dHsp8:1pcLQN:ugscYd1y27i-Auq_rvd1_l5eBuzpog-0YKQlmaA02PY', '2023-03-29 07:19:51.094430'),
('l0l4hexj8j9bo8i9k6ms23z1c4hpurnh', '.eJy1lE1v2zAMhv8K4csunmE7Tpzk1mRDV2ADgjlbMWxFQMu0rdWRAklOUAz775M_8tUGPTTYzZbIly8fSvrjrLA25arWpFY8c6ZO5LinaymyRxLNRvYbRSE9JoVRPPWaEK_f1d4XmVE162PPBErUZZMdEI3ziT-KUj8OxtGI4jifhBiNw2AQD30_HgQ48DFkYTZibDykKPaHecTCKBjGyKxoWsniLiO0ap_kDpYS7hU3BAi3UmYws9uwkNpMbewjPe2kyrSNTRgKgWlF7lfShIqV7neua6zgoyiwoDUJYzOwzjgJRk3GGqsK0lpzQVq7kMjc7FARMLneoHhyoZJZQWr_Dy5wYUgJMmBb3nJGsFFyyzNSve-l3HBm3fx0Ag-WfKMhl6r1z0VhOziYPLbRRvyQtYLOz6z3A7-EFQ09aCAYCfuu2nhTEixI5cTMRaV9J_Peeas18OAFkemJuaPQskQD99y6mePG8C1a_K3w5w5IL_tOw02Ps6sQebCwQEhAYpRNKjg9IyC62s33Bd93e7xJj3fR423kHzrEie2ZS9FChuCAZ39GXiX8qr7rgKW9x_x-hpqy533MFeZXN2ILDU5Ox1Hz5Xjeom2HMPyPY7AVhh7cIhdN9o0x1qadB-y4Ka8VHh3G-U0TfECDJ6O9Tjr2TkE3B5iq6o1aYw8C_8L1vs7h5Kz5xEj1ZHqPdm2uCK-nEPje1XanMCMbuFBoLyLrT9b520Wnr2n3WPBmDUXWPiFNycOy8_D3H9YKR9c:1pZ6ws:YVmkKuohDohAtMS6-xnxZri9tZkn-J7sc_aqwWUnBlU', '2023-03-20 09:16:02.338512'),
('l3n9423riet9h1s4sjosdfq4tz4kpwc0', '.eJxVjEEOwiAQRe_C2hCgQ4e6dN8zkOkwlaqBpLQr491Nky50-997_60i7VuOe5M1LkldFajL7zYRP6UcID2o3KvmWrZ1mfSh6JM2PdYkr9vp_h1kavmorUiYB9PDZNAG6AVxHhxBcLZDbwx2ljpDjl3qmYMXQONnYAfWI7H6fAHAijbc:1pZRhD:dRJKpyE-dwMhWWiH3Wa492Qddd5ttxfn2w4XmVXW8og', '2023-03-21 07:25:15.651792'),
('m3h2p5tv5k5puw0i7jbr47v1c0xgmzva', '.eJxVjDEOwyAQBP9CHSGMfRxOmd5vQMAdwUkEkrGrKH-PLblIim12ZvctnN_W7LbGi5tJXEUnLr9d8PHJ5QD08OVeZaxlXeYgD0WetMmpEr9up_t3kH3L-5pjQA2ICKpDZQayUUedQKlk0oB9z34PWG1otESRzAgeAygNxEGz-HwBy303qw:1pZO6o:CeKf73QRA74uUYot7Z7CI9xyEoeHQI7CUPZ4L70i8_w', '2023-03-21 03:35:26.229319'),
('msytv8kugpuu1yzyo6h3ppdoy46wp3dp', '.eJxVjDEOwyAQBP9CHSGMfRxOmd5vQMAdwUkEkrGrKH-PLblIim12ZvctnN_W7LbGi5tJXEUnLr9d8PHJ5QD08OVeZaxlXeYgD0WetMmpEr9up_t3kH3L-5pjQA2ICKpDZQayUUedQKlk0oB9z34PWG1otESRzAgeAygNxEGz-HwBy303qw:1pZ3Sr:mcUObjVdGkw6nR-hVZdVtJeJtXPQpqswDmI7vF7sYos', '2023-03-20 05:32:49.864022'),
('nf4xtwot0o5ase4zjofhuwgxlnf46bpv', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1peWFU:Q5w1XxvziYdL3L4UDXmMuJ73Zq1mfkeF--2uov8PiqI', '2023-04-04 07:17:36.519445'),
('o6xb1k5esohrahu99qu6woh42n901x27', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pc1xm:FaBQJy4oOIOZQ3y4N0oRB9TeY3F6Vf6nP8GFA1f9JHc', '2023-03-28 10:33:02.989838'),
('ogksu27n55kxg3tkv1f63fz15splrfl5', '.eJxVjDEOwyAQBP9CHSGMfRxOmd5vQMAdwUkEkrGrKH-PLblIim12ZvctnN_W7LbGi5tJXEUnLr9d8PHJ5QD08OVeZaxlXeYgD0WetMmpEr9up_t3kH3L-5pjQA2ICKpDZQayUUedQKlk0oB9z34PWG1otESRzAgeAygNxEGz-HwBy303qw:1paa5E:M2En0nrCIhyFpPqYigXaRcpLUK5d6-Rz5U7ysOHseCM', '2023-03-24 10:34:44.354216'),
('op829j6qbu67o0jilo4mkacgr5on8atg', '.eJxVjEEOwiAQRe_C2hCgQ4e6dN8zkOkwlaqBpLQr491Nky50-997_60i7VuOe5M1LkldFajL7zYRP6UcID2o3KvmWrZ1mfSh6JM2PdYkr9vp_h1kavmorUiYB9PDZNAG6AVxHhxBcLZDbwx2ljpDjl3qmYMXQONnYAfWI7H6fAHAijbc:1pZUHV:u8xm6e4oHjjPgltPTDC0ZsbGmzyydqpWen5Ueg1sLnA', '2023-03-21 10:10:53.683097'),
('orp1mi9dsdzv8l73kcqd4heullxyrdm0', '.eJyVkF9LwzAUxb_KpU8Ks3Rt19qCIj4IexCFCT5so9wmt2tmTWqS_YGx727adeAEHwzk5ZyT8zvk4BW4sXWxMaQLwb3ci73RT61E9kGyM_ga5Ur5TEmrRel3EX9wjf-sODWPQ_aioEZTu9fRJKYwCipKGMZJEIVxQjzNMGNZlYzDJCUMIwpvKeYRjSdxGgQ8zKKyCtMEkUeudEelK3po1ErIQtPXRmjiALDQC8mpAod7p_JNtYJddTYZO9oNwnXepVwYuv20t3AHh2Onna_Tt6Qt2FoYENIqWOMWDdOitXB-3J3Tkr7VePncOzkL2bo1gtlXrUqEPIepJY1lQ_OZ-y-5WsLNPcyn0i5_Rfduyie2MIgvknrdwN5b9qgZMSuUHGB_g-CC9NQo_Bfr-A0hX7LV:1periz:H_WXsWiUiqSm806dBG3VBGWiWaWnk9ubY-O165KwFZ0', '2023-04-05 06:13:29.295792'),
('ott6tbjo0zemjvs7tj3zmzva78orretn', '.eJy1VNFu2koQ_ZURT0HiUmIoaSLlwQFTLIGNbKdp1FTR2juEvbV30e46FFX33-8s2Co0eS0PZtmZc-bMzMG_Os-stpvn2qB-Frxz0xl1eqd3OSt-oHQB_i-TL6pfKGm1yPsupd9ETX-pOJZ3Te4ZwYaZDaGHH0foDQdrHBdsNB4MvdEY-dU1uy6u1-NLb3yFzBui9wlHfIiXH0dXgwH3rof52rsaM8aHRLrDnIiKkhkDD5inWFih5EXlSjcKujdP-klC87HClghwC9DkTDZMzwSW_AIq9vO5RPliN7feYNA9heWK709RGf60R5Ssy_I20zX2IC-Z_HE4n2F3SvOJqqV9r-i78N57Uo7dZmorCtO5-db5QBdUhJ4wUdu9Fi8bCxdFF7zB5fAfeox78CAkh0S8ooZ0byxWpgehLPpHXINOkAvj9le72QEjCG0JhASjal3g4SYXkuk9rJV2HDthN6D04VvV1rUl1qJgjqAHTGNDvUVdCWuRw1arV8HpYDfM0gOJqizVTsgXIPtw4aDGQaFCe3Mm8LL7h0YDat2KK2iiUNXGgkbLSLTjZrl6daF2LFJZUWCv4bMbYaAkPkdzWlzyP5RRUfKWqFCfj8x7q4gqn8yoVURt85pU_h1R0LTLVVFXKC1rF_hB6YZWUVyTnSxqwUrzew-HFR7AJ22cdznsQoTiQOASJavQiXtrKmrld8phOcIaaN4KtVXakII95K0tyF7UlAJ6MVAMnZNIV6UswnFghOYk-JXS1hQ4Dseotd05g7SuM1ssnO1as2nhLKmd4eTResa8aSqbhymk8Sx78JMA6LxK4i_hNJjC3SMFA5jEq8ck_DzPYB4vpkGSgh9N6TbKkvDuPovp4qnjpwR9ajldgh89QvB1lQRpCnEC4XK1CImUqiR-lIVBSv-8aLK4n4bR5x4QEURxBotwGWaUlsU9V7zhewuGeAbLIJnM6ad_Fy7C7PFQdRZmkas4o5I-rPwkCyf3Cz-B1X2yitOW0LU6DdPJwg-XwbRPSqg6BF-CKIN07i8W73bu-mj67nz_73-52_tz:1pe9Sc:M4QM7kk-pF92-KBJ7V4-hrNJuGCwHMsaRvJGhjo0mdI', '2023-04-03 06:57:38.427584'),
('oza0e3bb6xzj03f6nmxp6113s0gs6ehf', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pcLAc:utmBi_RM9nCoqF2i5RXBswNjzIOykPrt8mfX9FkSstw', '2023-03-29 07:03:34.983924'),
('pahmo7jm5tq4zhv0lwc0krnymqq202v8', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pcKLE:UZWk0WU3MshdLWyM0Sv9a3mRO7Aw4HyTLTHISw9MWFM', '2023-03-29 06:10:28.257257'),
('rwah2edl8y9of8amscj280t96w5zdjwa', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pc1xE:AErCfQBFP1MpEP9gWT6f2SPFdsO-k17r67kxdTc8tVM', '2023-03-28 10:32:28.496849'),
('scwg1qt3j96p7xki3czwhjolowv5xtrr', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pfGuW:TnZcPqcFbheYnErQUYF3oUQTx30fto03DdGYqHwH05s', '2023-04-06 09:07:04.647500'),
('shuk6bhrfw6di5q3vxwfiswqymj5i5gi', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pcKnb:XTp1eHeKSrkEJCMtxwiQr1AEFAw1sRv_GNTMXaeoOoY', '2023-03-29 06:39:47.390162'),
('vawf8z0zrmnrl6sxpiey1dsen7dzbhdx', '.eJyNksFu00AQhl9l5HNkObZjkx5bRaWHqhUJcAAUjXfH9lBn19pdExXEuzNOnEBbAT1Zuzv_N9-M_CPa4hDa7eDJbVlHF1Eezf68q1A9kBkf9Fc0jY2VNcFxFY8l8fTq41urqbucap8AWvStpLNFTmmW1FQozIskS_OCdLnEpVrWxTwtSsI0o_QN5Tqj-SIvk0Sny6yq07JA1JlAq842N5pQaG_tHjYWPjoOBAjX1mq4lGe4tz5cSO0DPe6t015q1wqNwaqj2TvyhE61sw_sB-xgZRpsaEcmSAIHzWQUScLbOuzREZBp2BA5mLpvbM9KmJ-ieQzrQD1Uj8fv9cCaIByV2DQidWV3PXXdeDirQW0drE_41YT38NlIhzSGcS6B3BjVDcI7qwvMBPEENi_jpw4TJothnsCGe3_odhI6DPtExv_TJj_bvPcEx4358bgyLcqe_u4xwQ-URQynrcuiHAZqmJ6J1TWpwN9eSSzil7OtV3dw1wfe8XfSr8OUv8cL3ElOYorlp7glzTje3zu7s-G_VtGXn78AmNcd6w:1pcLkR:HOVPZfZQAbeUtPGxiFdc9bfRrshQEJ3AN3O0wWOZTAo', '2023-03-29 07:40:35.384003'),
('w4cj1pkfjf0z87qup7neghnie0y9r4vc', '.eJxVjEEOgjAQRe_StWnKzNBal-45Axk6g6CmTSisjHdXEha6_e-9_zI9b-vUb1WXfhZzMWROv9vA6aF5B3LnfCs2lbwu82B3xR602q6IPq-H-3cwcZ2-NbakgG5Un5i8QyCvEiLHFEffgA_KgApnJUFtWgrOCUQcRgieWdC8P8-sN3E:1pcMC4:b3ws5e9PMJMcjXoniqvd8qBlQTfpnQB5qaXd73t6tjQ', '2023-03-29 08:09:08.263962'),
('zwfv1ve7yasv262s69d756mmvq55psd8', '.eJyFkVGP2jAQhP_KKs-RBUlICo-gU3tSTz0V1Kq6Vmhjb4JLsJHtgE5V_3ttkpRU3PUend2ZfDP7K9pi63bb1pLZShEtoiyKx99K5HtSYSB-oqo141o5I0sWVlg_texBC2qW_e4_Bju0O69OZxkl6aSinGOWT9Iky0kUc5zzeZVPk7wgTFJK3lEmUprOsmIyEck8LaukyBFF6k3LRtf3gtC7fdBn2Gj4aqQjQHivtYClH8Ojtm7hd_f0fNZGWL-75qgUlg3Fn8kSGr6Lv0jbYgN3qsaaDqScV2ArJClOQXHApoGytVKRtTGsdeXOaAi4PhxRPcfQaFGTGd4Qg1SOjCIHPvJJcoKj0ScpyPTcG32U3NM8RVMGgd5d6f8CjiLARh4tVNpAB7PsYch-V94yYTCEgbUz6KiWZIPpypB_ddGkqmHlz-UDdlZDjtWFW_ZmKYObQhYD5APuCb7p1lzhrP8lKgGf2s72oy-j-9XYNWOeBSsXJndVRdzJE41NgvR-qG3d1_bY19Z5zNilpGBxc-TXG4IA90rW_OoYpOPAox5fTHWxfQO4YN0BgvB61v4G_0GOX-CNbxHiNxiiH7__ACV0UwQ:1pcOQ9:TJdwe4CzpGYKG56bUKWKdJbsP5nx8d-aGPFDpD4uAAg', '2023-03-29 10:31:49.934927');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `dashboard_blog`
--
ALTER TABLE `dashboard_blog`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `dashboard_blog_profile_id_bb95cd99_fk_dashboard_profile_id` (`profile_id`);

--
-- Indexes for table `dashboard_blogsection`
--
ALTER TABLE `dashboard_blogsection`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `dashboard_blogsection_blog_id_7c8130dc_fk_dashboard_blog_id` (`blog_id`);

--
-- Indexes for table `dashboard_profile`
--
ALTER TABLE `dashboard_profile`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `dashboard_profile_recommended_by_id_5efb3d50_fk_auth_user_id` (`recommended_by_id`);

--
-- Indexes for table `dashboard_web`
--
ALTER TABLE `dashboard_web`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `dashboard_web_profile_id_119ff2b6_fk_dashboard_profile_id` (`profile_id`);

--
-- Indexes for table `dashboard_websection`
--
ALTER TABLE `dashboard_websection`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `dashboard_websection_web_id_9a33ef63_fk_dashboard_web_id` (`web_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `dashboard_blog`
--
ALTER TABLE `dashboard_blog`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `dashboard_blogsection`
--
ALTER TABLE `dashboard_blogsection`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `dashboard_profile`
--
ALTER TABLE `dashboard_profile`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `dashboard_web`
--
ALTER TABLE `dashboard_web`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `dashboard_websection`
--
ALTER TABLE `dashboard_websection`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `dashboard_blog`
--
ALTER TABLE `dashboard_blog`
  ADD CONSTRAINT `dashboard_blog_profile_id_bb95cd99_fk_dashboard_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `dashboard_profile` (`id`);

--
-- Constraints for table `dashboard_blogsection`
--
ALTER TABLE `dashboard_blogsection`
  ADD CONSTRAINT `dashboard_blogsection_blog_id_7c8130dc_fk_dashboard_blog_id` FOREIGN KEY (`blog_id`) REFERENCES `dashboard_blog` (`id`);

--
-- Constraints for table `dashboard_profile`
--
ALTER TABLE `dashboard_profile`
  ADD CONSTRAINT `dashboard_profile_recommended_by_id_5efb3d50_fk_auth_user_id` FOREIGN KEY (`recommended_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `dashboard_profile_user_id_3e392fce_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `dashboard_web`
--
ALTER TABLE `dashboard_web`
  ADD CONSTRAINT `dashboard_web_profile_id_119ff2b6_fk_dashboard_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `dashboard_profile` (`id`);

--
-- Constraints for table `dashboard_websection`
--
ALTER TABLE `dashboard_websection`
  ADD CONSTRAINT `dashboard_websection_web_id_9a33ef63_fk_dashboard_web_id` FOREIGN KEY (`web_id`) REFERENCES `dashboard_web` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
