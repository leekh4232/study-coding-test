/*M!999999\- enable the sandbox mode */
-- MariaDB dump 10.19-11.4.5-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: clonebose
-- ------------------------------------------------------
-- Server version	11.4.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '관리자 일련번호',
  `admin_email` varchar(320) NOT NULL COMMENT '관리자 로그인 ID',
  `admin_password` varchar(255) NOT NULL COMMENT '관리자 로그인 비밀번호 (암호화)',
  `admin_name` varchar(50) NOT NULL COMMENT '관리자 이름',
  `admin_gender` enum('남','여') NOT NULL COMMENT '관리자 성별',
  `admin_phone` varchar(20) NOT NULL COMMENT '관리자 연락처',
  `admin_birthdate` date NOT NULL COMMENT '관리자 생년월일',
  `reg_date` datetime NOT NULL COMMENT '가입한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '가입 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carts`
--

DROP TABLE IF EXISTS `carts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `carts` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '장바구니 정보 일련번호',
  `user_id` int(11) NOT NULL COMMENT '회원 정보',
  `product_id` int(11) NOT NULL COMMENT '상품 정보',
  `reg_date` datetime NOT NULL COMMENT '장바구니에 추가한 날짜 시간 정보',
  PRIMARY KEY (`cart_id`),
  KEY `carts_users_FK` (`user_id`),
  KEY `carts_products_FK` (`product_id`),
  CONSTRAINT `carts_products_FK` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `carts_users_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carts`
--

LOCK TABLES `carts` WRITE;
/*!40000 ALTER TABLE `carts` DISABLE KEYS */;
/*!40000 ALTER TABLE `carts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '카테고리 일련번호',
  `category_name` varchar(100) NOT NULL COMMENT '상위 카테고리명',
  `reg_date` datetime NOT NULL COMMENT '하위  카테고리 정보를 등록한 날짜 시간 정보',
  `edit_date` varchar(100) NOT NULL COMMENT '하위  카테고리 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES
(1,'상품 카테고리','2025-06-15 10:00:00','2025-06-15 10:00:00');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colors`
--

DROP TABLE IF EXISTS `colors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `colors` (
  `color_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '색상 일련번호',
  `color_name` varchar(50) NOT NULL COMMENT '색상명',
  `color_code` varchar(10) NOT NULL COMMENT '색상 코드',
  `reg_date` datetime NOT NULL COMMENT '색상 정보를 등록한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '색상 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`color_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colors`
--

LOCK TABLES `colors` WRITE;
/*!40000 ALTER TABLE `colors` DISABLE KEYS */;
INSERT INTO `colors` VALUES
(1,'검정색','#000','2025-06-15 10:00:00','2025-06-15 10:00:00');
/*!40000 ALTER TABLE `colors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notices`
--

DROP TABLE IF EXISTS `notices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `notices` (
  `notice_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '공지 일련번호',
  `admin_id` int(11) NOT NULL COMMENT '작성한 관리자 정보',
  `notice_title` varchar(200) NOT NULL COMMENT '공지 제목',
  `notice_content` text NOT NULL COMMENT '공지 내용',
  `notice_img` varchar(255) DEFAULT NULL COMMENT '공지 이미지',
  `reg_date` datetime NOT NULL COMMENT '가입한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '가입 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`notice_id`),
  KEY `notices_admins_FK` (`admin_id`),
  CONSTRAINT `notices_admins_FK` FOREIGN KEY (`admin_id`) REFERENCES `admins` (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notices`
--

LOCK TABLES `notices` WRITE;
/*!40000 ALTER TABLE `notices` DISABLE KEYS */;
/*!40000 ALTER TABLE `notices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '주문 정보 일련번호',
  `user_id` int(11) NOT NULL COMMENT '회원 정보',
  `order_status` varchar(20) NOT NULL COMMENT '주문 상태',
  `order_quantity` int(11) NOT NULL COMMENT '주문 수량',
  `order_total_price` int(11) NOT NULL COMMENT '주문 총금액',
  `reg_date` datetime NOT NULL COMMENT '주문 정보를 등록한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '주문 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`order_id`),
  KEY `orders_users_FK` (`user_id`),
  CONSTRAINT `orders_users_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_products`
--

DROP TABLE IF EXISTS `orders_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_products` (
  `order_product_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '주문 상품 정보 일련번호',
  `order_id` int(11) NOT NULL COMMENT '주문 정보',
  `category_id` int(11) NOT NULL COMMENT '카테고리 정보',
  `color_id` int(11) NOT NULL COMMENT '주문 상품 색상 정보',
  `order_product_name` varchar(200) NOT NULL COMMENT '주문 상품명',
  `order_product_price` int(11) NOT NULL COMMENT '주문 상품 금액',
  `order_product_img` varchar(255) NOT NULL COMMENT '주문 상품 이미지',
  `order_product_origin` varchar(50) NOT NULL COMMENT '상품 원산지',
  `reg_date` datetime NOT NULL COMMENT '주문 상품 정보를 등록한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '주문 상품 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`order_product_id`),
  KEY `orders_products_orders_FK` (`order_id`),
  KEY `orders_products_categories_FK` (`category_id`),
  KEY `orders_products_colors_FK` (`color_id`),
  CONSTRAINT `orders_products_categories_FK` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`),
  CONSTRAINT `orders_products_colors_FK` FOREIGN KEY (`color_id`) REFERENCES `colors` (`color_id`),
  CONSTRAINT `orders_products_orders_FK` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_products`
--

LOCK TABLES `orders_products` WRITE;
/*!40000 ALTER TABLE `orders_products` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '상품 일련번호',
  `category_id` int(11) NOT NULL COMMENT '상품 카테고리 정보',
  `color_id` int(11) NOT NULL COMMENT '상품 색상 정보',
  `product_name` varchar(200) NOT NULL COMMENT '상품명',
  `product_price` int(11) NOT NULL COMMENT '상품 금액',
  `product_img` varchar(255) NOT NULL COMMENT '상품 이미지',
  `product_description_img` varchar(255) NOT NULL COMMENT '상품 설명 이미지',
  `product_origin` varchar(50) NOT NULL COMMENT '상품 원산지',
  `product_stock` int(11) NOT NULL COMMENT '상품 재고',
  `reg_date` datetime NOT NULL COMMENT '상품 정보를 등록한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '상품 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`product_id`),
  KEY `products_categories_FK` (`category_id`),
  KEY `products_colors_FK` (`color_id`),
  CONSTRAINT `products_categories_FK` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`),
  CONSTRAINT `products_colors_FK` FOREIGN KEY (`color_id`) REFERENCES `colors` (`color_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES
(1,1,1,'상품이름',3000,'img','123','123',123,'2025-06-15 10:00:00','2025-06-15 10:00:00'),
(2,1,1,'상품 이이이이름',6000,'img2','456','456',456,'2025-06-15 10:00:00','2025-06-15 10:00:00');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_colors`
--

DROP TABLE IF EXISTS `products_colors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_colors` (
  `product_color_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '상품-색상 관계 일련번호',
  `product_id` int(11) NOT NULL COMMENT '상품 일련번호',
  `color_id` int(11) NOT NULL COMMENT '상품 별 가능 색상 일련번호',
  `reg_date` datetime NOT NULL COMMENT '색상 정보를 등록한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '색상 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`product_color_id`),
  KEY `products_colors_products_FK` (`product_id`),
  KEY `products_colors_colors_FK` (`color_id`),
  CONSTRAINT `products_colors_colors_FK` FOREIGN KEY (`color_id`) REFERENCES `colors` (`color_id`),
  CONSTRAINT `products_colors_products_FK` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_colors`
--

LOCK TABLES `products_colors` WRITE;
/*!40000 ALTER TABLE `products_colors` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_colors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sub_categories`
--

DROP TABLE IF EXISTS `sub_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `sub_categories` (
  `sub_category_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '하위 카테고리 일련번호',
  `category_id` int(11) NOT NULL COMMENT '상위 카테고리 일련번호',
  `sub_category_name` varchar(100) NOT NULL COMMENT '하위 카테고리명',
  `reg_date` datetime NOT NULL COMMENT '하위  카테고리 정보를 등록한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '하위  카테고리 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`sub_category_id`),
  KEY `sub_categorys_categories_FK` (`category_id`),
  CONSTRAINT `sub_categorys_categories_FK` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sub_categories`
--

LOCK TABLES `sub_categories` WRITE;
/*!40000 ALTER TABLE `sub_categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `sub_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '회원 일련번호',
  `user_email` varchar(320) NOT NULL COMMENT '사용자 로그인 ID 및 이메일',
  `user_password` varchar(255) NOT NULL COMMENT '사용자 로그인 비밀번호 (암호화)',
  `user_name` varchar(50) NOT NULL COMMENT '사용자 이름',
  `user_gender` enum('남','여') NOT NULL COMMENT '사용자 성별',
  `user_phone` varchar(20) NOT NULL COMMENT '사용자 연락처',
  `user_birthdate` date NOT NULL COMMENT '사용자 생년월일',
  `user_address` varchar(255) NOT NULL COMMENT '사용자 주소',
  `user_profile_img` varchar(255) NOT NULL COMMENT '사용자 프로필 이미지',
  `reg_date` datetime NOT NULL COMMENT '가입한 날짜 시간 정보',
  `edit_date` datetime NOT NULL COMMENT '가입 정보를 수정한 날짜 시간 정보',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='회원 정보를 저장하는 테이블';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(1,'apple@gmail.com','password111','양땡땡','남','010-7777-2222','2025-06-15','서울시','양땡땡얼굴사진','2025-06-15 10:00:00','2025-06-15 10:00:00'),
(2,'banana@naver.com','암호23242','권땡땡','남','010-4535-6575','1999-09-09','제주도','권떙땡얼굴사진','2025-01-02 15:00:00','2025-06-15 10:00:00'),
(3,'cat@space.com','passsssworddd','성땡땡','남','010-3295-2895','1990-09-15','울릉도','성땡땡 얼굴사진','2020-04-01 08:00:00','2025-06-15 10:00:00'),
(4,'wood@gmail.com','passsssss','정땡땡','여','010-1111-5965','1999-07-20','독도','정땡땡 얼굴사진','2000-01-15 07:00:00','2025-06-15 10:00:00');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wishlists`
--

DROP TABLE IF EXISTS `wishlists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `wishlists` (
  `wishlist_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '위시리스트 정보 일련번호',
  `user_id` int(11) NOT NULL COMMENT '회원 정보',
  `product_id` int(11) NOT NULL COMMENT '상품 정보',
  `reg_date` datetime NOT NULL COMMENT '위시리스트에 추가한 날짜 시간 정보',
  PRIMARY KEY (`wishlist_id`),
  KEY `wishlists_users_FK` (`user_id`),
  KEY `wishlists_products_FK` (`product_id`),
  CONSTRAINT `wishlists_products_FK` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`),
  CONSTRAINT `wishlists_users_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wishlists`
--

LOCK TABLES `wishlists` WRITE;
/*!40000 ALTER TABLE `wishlists` DISABLE KEYS */;
/*!40000 ALTER TABLE `wishlists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'clonebose'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-06-16 10:57:30