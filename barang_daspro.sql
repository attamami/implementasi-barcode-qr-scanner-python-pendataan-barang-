-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2020 at 01:50 AM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `barang_daspro`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang_daspro`
--

CREATE TABLE `barang_daspro` (
  `id` text DEFAULT NULL,
  `jumlah_barang` varchar(40) DEFAULT NULL,
  `harga` varchar(40) DEFAULT NULL,
  `merek` text DEFAULT NULL,
  `jenis_barang` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `barang_daspro`
--

INSERT INTO `barang_daspro` (`id`, `jumlah_barang`, `harga`, `merek`, `jenis_barang`) VALUES
('b\'0036000291452\'', '', '', '', ''),
('b\'0036000291452\'', '', '', '', ''),
('b\'Hello :)\'', '1', '2000', 'ABC', 'Sakatonik'),
('b\'0051111407592\'', '1', '64000', 'Toshiba 32GB', 'Flashdisk'),
('0036000291452', '2', '2000', 'kiko', 'permen'),
('19', '2', '5000', 'Soklin', 'Detergen'),
('b\'0036000291452\'', '', '', '', ''),
('0036000291452', '1', '64000', 'Samsung', 'Flashdisk 32GB'),
('67', '1', '500', 'Relaxa', 'Permen');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
