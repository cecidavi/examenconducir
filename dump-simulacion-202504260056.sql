/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.7.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: simulacion
-- ------------------------------------------------------
-- Server version	11.7.2-MariaDB

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
-- Table structure for table `banco_imagenes`
--

DROP TABLE IF EXISTS `banco_imagenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `banco_imagenes` (
  `codigo_imagen` int(11) NOT NULL,
  `ruta` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`codigo_imagen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banco_imagenes`
--

LOCK TABLES `banco_imagenes` WRITE;
/*!40000 ALTER TABLE `banco_imagenes` DISABLE KEYS */;
INSERT INTO `banco_imagenes` VALUES
(1,'NULL'),
(2,'null'),
(3,'null'),
(4,'null'),
(5,'null'),
(6,'/static/img/sp-18.png'),
(7,'NULL'),
(8,'NULL'),
(9,'NULL'),
(10,'NULL'),
(11,'NULL'),
(12,'/static/img/sp-33.png'),
(13,'NULL'),
(14,'NULL'),
(15,'NULL'),
(16,'NULL'),
(17,'NULL'),
(18,'NULL'),
(19,'NULL'),
(20,'NULL'),
(21,'NULL'),
(22,'NULL'),
(23,'NULL'),
(24,'NULL'),
(25,'NULL'),
(26,'NULL'),
(27,'NULL'),
(28,'NULL'),
(29,'NULL'),
(30,'NULL'),
(31,'NULL'),
(32,'NULL'),
(33,'NULL'),
(34,'NULL'),
(35,'NULL'),
(36,'NULL'),
(37,'NULL'),
(38,'NULL'),
(39,'/static/img/sr-25.png'),
(40,'/static/img/sr-25a.png'),
(41,'/static/img/sr-24.png'),
(42,'/static/img/sr-22.png'),
(43,'/static/img/sr-26.png'),
(44,'NULL'),
(45,'NULL'),
(46,'NULL'),
(47,'NULL'),
(48,'NULL'),
(49,'NULL'),
(50,'NULL');
/*!40000 ALTER TABLE `banco_imagenes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiante`
--

DROP TABLE IF EXISTS `estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante` (
  `matricula` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) DEFAULT NULL,
  `paterno` varchar(30) DEFAULT NULL,
  `materno` varchar(30) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefono` bigint(20) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=20230018 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante`
--

LOCK TABLES `estudiante` WRITE;
/*!40000 ALTER TABLE `estudiante` DISABLE KEYS */;
INSERT INTO `estudiante` VALUES
(20230001,'Juan','Pérez','López','juan@example.com',8441230001,'1234'),
(20230002,'Ana','Ramírez','Santos','ana@example.com',8441230002,'1234'),
(20230003,'Luis','Gómez','Martínez','luis@example.com',8441230003,'1234'),
(20230004,'Sofía','Díaz','Vega','sofia@example.com',8441230004,'1234'),
(20230005,'Carlos','Hernández','Ruiz','carlos@example.com',8441230005,'1234'),
(20230006,'ejemplo','apellidoeejemplo','otravez','aaaa@example.com',8440000000,'0000'),
(20230007,'cecilio','sanchez','hernandez','cecilio@example.com',8441044850,'scrypt:32768:8:1$Ri1E16i3InimTxxK$7e9dcce87d92dd084e9a1b7cd38c79b87776242099dfffcaac61ad8eb77b623e7427e4c61c35841c1e842e326cff28e3c23d062a9b01cc87b39069948df90c9a'),
(20230008,'ana','sofia','castillo','anasofi@example.com',8888888888,'scrypt:32768:8:1$gLirBzRXHStTH9EQ$b9793e7ef22acf6e8a0c18be2534939c85277943011905c927373e06e1b404f2ff3f47a8cb871252f8a6ac6ae97628115bc074c541b45310bcc6054e86d18204'),
(20230009,'Erick','Agustin','castillo','Ecas@example.com',8446754183,'scrypt:32768:8:1$Qf9RFfHy1JKkYok9$aa37d2d1469b945e0acb269bc89a3cbec4c4ef83a49e039b620337eaa564393cbcb5487aacb8be648eae8981a5634b04b97b5f8940f371dbfeffa4c6814b8179'),
(20230010,'qwe','asd','zxc','zxc@example.com',1,'scrypt:32768:8:1$HsjKt8EhrLRFy8gf$a23e62ddfde6334692b7bd43f7524249ef4ffbe378b14270ddf4daaf2f8053a72bd5fbbe7b171f5ac281e5c622ba77840ecedf8482b9a99fdda1d18d77686d01'),
(20230011,'prueba2','prueba2','prueba2','prueba2@example.com',77777777,'scrypt:32768:8:1$N7mK8u3K4iptXAyU$d03c3862c40bc0cdd123514abeefd90ae1d449e9b93b54dcc06ce0e36e297dba201fe00a87a5bc4d2ce5c0a2e4b3c6bf4057793504649912699a963a1d5758a0'),
(20230012,'ejemplo','apellidoeejemplo','otravez','aaaa@example.com',8440000000,'0000'),
(20230013,'ejemplo','apellidoeejemplo','otravez','aaaa@example.com',8440000000,'0000'),
(20230014,'ejemplo','apellidoeejemplo','otravez','aaaa@example.com',8440000000,'0000'),
(20230015,'prueba3','prueba3','prueba3','prueba3@example.com',8888888888,'scrypt:32768:8:1$01kO67PL7IQ7kKSo$176ca8973c1b1c8bf39f162e3eb590f9c800ce1ee8de16b47a044d3f78c86899c875ee527e0b5d07e4f8aaa76fa43450db64dd80e428c581685ee6682a116ede'),
(20230016,'prueba4','prueba4','prueba4','prueba4@example.com',9999999999,'scrypt:32768:8:1$BKisKt6bKACEmQWZ$9903bcc1d46d894269cd88df67b93df6c1b9ad1d30fdf30d05f560b891d3df365ea37ad165c1a4be25e898c4bead21a4e51098c5dbd86d58d9aa9be5a56c894f'),
(20230017,'prueba5','prueba5','prueba5','prueba5@example',4444444,'scrypt:32768:8:1$slzMYtY8v5UwMnL6$e3e28a197693d3b89a120bfbac09c92812914fafffde61c09d123926abc3309eedf5d6b60ac61f4000164eb3830ec9930562cfbce9e3b8eae6690c71272243f1');
/*!40000 ALTER TABLE `estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examen_estudiante`
--

DROP TABLE IF EXISTS `examen_estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `examen_estudiante` (
  `id_seleccion` int(11) NOT NULL,
  `id_pregunta` int(11) DEFAULT NULL,
  `matricula` bigint(20) DEFAULT NULL,
  `respuesta` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_seleccion`),
  KEY `id_pregunta` (`id_pregunta`),
  KEY `matricula` (`matricula`),
  CONSTRAINT `examen_estudiante_ibfk_1` FOREIGN KEY (`id_pregunta`) REFERENCES `preguntas` (`id_pregunta`),
  CONSTRAINT `examen_estudiante_ibfk_2` FOREIGN KEY (`matricula`) REFERENCES `estudiante` (`matricula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examen_estudiante`
--

LOCK TABLES `examen_estudiante` WRITE;
/*!40000 ALTER TABLE `examen_estudiante` DISABLE KEYS */;
/*!40000 ALTER TABLE `examen_estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_estudiante`
--

DROP TABLE IF EXISTS `historial_estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_estudiante` (
  `id_record` int(11) NOT NULL AUTO_INCREMENT,
  `matricula` bigint(20) DEFAULT NULL,
  `tipo_test` varchar(15) DEFAULT NULL,
  `fecha_hora_realiza` datetime DEFAULT NULL,
  `calificacion` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id_record`),
  KEY `matricula` (`matricula`),
  CONSTRAINT `historial_estudiante_ibfk_1` FOREIGN KEY (`matricula`) REFERENCES `estudiante` (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_estudiante`
--

LOCK TABLES `historial_estudiante` WRITE;
/*!40000 ALTER TABLE `historial_estudiante` DISABLE KEYS */;
INSERT INTO `historial_estudiante` VALUES
(1,20230001,'practica','2025-04-25 22:22:41',50.00),
(2,20230001,'practica','2025-04-25 22:29:08',30.00),
(3,20230001,'practica','2025-04-25 22:29:46',25.00),
(4,20230001,'practica','2025-04-25 22:30:29',35.00),
(5,20230001,'practica','2025-04-25 22:30:59',40.00),
(6,20230001,'practica','2025-04-25 22:31:44',35.00),
(7,20230001,'final','2025-04-25 23:54:07',42.50),
(8,20230001,'final','2025-04-25 23:55:30',37.50),
(9,20230001,'final','2025-04-25 23:56:57',32.50),
(10,20230002,'practica','2025-04-26 00:29:25',75.00);
/*!40000 ALTER TABLE `historial_estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preguntas`
--

DROP TABLE IF EXISTS `preguntas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `preguntas` (
  `id_pregunta` int(11) NOT NULL,
  `codigo_imagen` int(11) DEFAULT NULL,
  `reactivo` varchar(250) DEFAULT NULL,
  `tipo_etiqueta_html` char(1) DEFAULT NULL,
  PRIMARY KEY (`id_pregunta`),
  KEY `codigo_imagen` (`codigo_imagen`),
  CONSTRAINT `preguntas_ibfk_1` FOREIGN KEY (`codigo_imagen`) REFERENCES `banco_imagenes` (`codigo_imagen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preguntas`
--

LOCK TABLES `preguntas` WRITE;
/*!40000 ALTER TABLE `preguntas` DISABLE KEYS */;
INSERT INTO `preguntas` VALUES
(1,1,'Antes de encender el vehículo, el conductor deberá:','P'),
(2,NULL,'¿En qué parte del vehículo deben viajar los niños?','P'),
(3,NULL,'Si usted conduce un vehículo en estado de ebriedad o bajo la influencia de algún estupefaciente, está cometiendo:','P'),
(4,NULL,'Cuando un vehículo de emergencia circula con códigos encendidos y sirena, ¿qué debe hacer?','P'),
(5,NULL,'¿Cuándo se puede estacionar en lugares reservados para personas con discapacidad?','P'),
(6,6,'¿Qué significa esta señalética?','P'),
(7,NULL,'Usar teléfono u otro aparato de radiocomunicación mientras conduce se considera:','P'),
(8,NULL,'Las placas, el engomado y la tarjeta de circulación son documentos:','P'),
(9,NULL,'En caso de que un agente de tránsito le indique en vía pública que se detenga, ¿quién debe bajar del vehículo?','P'),
(10,NULL,'Las señales de color negro sobre fondo amarillo son:','P'),
(11,NULL,'¿Cuál es el significado de la luz ámbar o amarilla en los semáforos?','P'),
(12,12,'¿Qué significa esta señalética?','P'),
(13,NULL,'Antes de iniciar la conducción, ¿qué puntos básicos de seguridad del vehículo debe revisar?','P'),
(14,NULL,'¿Cuándo es necesario llevar encendidas las luces delanteras y traseras de su vehículo?','P'),
(15,NULL,'Está prohibido que los vehículos porten en el parabrisas y ventanillas:','P'),
(16,NULL,'Se prohíbe usar en vehículos particulares este tipo de luces y sonidos.','P'),
(17,NULL,'Si usted va conduciendo su vehículo y es testigo de un accidente, ¿cómo debe proceder?','P'),
(18,NULL,'Si usted se ve implicado en un accidente en donde solo existen daños materiales, ¿Cómo debe proceder?','P'),
(19,NULL,'Si usted incurre en alguna infracción, ¿qué garantías puede retenerle la autoridad?','P'),
(20,NULL,'De las siguientes afirmaciones, ¿cuál es la interpretación correcta de las luces de los semáforos?','P'),
(21,NULL,'¿Cómo se clasifican las señales de tránsito?','P'),
(22,NULL,'Si existe línea continua, ¿puedo cambiar de carril?','P'),
(23,NULL,'¿Está permitido consumir bebidas alcohólicas dentro de un auto en circulación?','P'),
(24,NULL,'¿En dónde está señalado el número de pasajeros que se puede transportar en un vehículo?','P'),
(25,NULL,'¿Cuándo puede circular sin una o ambas placas de circulación?','P'),
(26,NULL,'¿Qué distancia debes guardar con el vehículo que esté adelante mientras te desplazas?','P'),
(27,NULL,'Está prohibido que viajen en el asiento contiguo al conductor del vehículo:','P'),
(28,NULL,'Si un vehículo busca rebasarte ¿qué debes hacer?','P'),
(29,NULL,'¿Cuál es la velocidad máxima en zonas urbanas?','P'),
(30,NULL,'¿Cuál es la velocidad máxima en zonas escolares?','P'),
(31,NULL,'La vuelta a la derecha, ¿es siempre continua?','P'),
(32,NULL,'¿Qué distancia puede recorrer un vehículo en reversa?','P'),
(33,NULL,'Al estacionarte, ¿cuál es la distancia máxima entre el auto y la banqueta?','P'),
(34,NULL,'¿Cómo debe dejar el vehículo si es estacionado en bajada?','P'),
(35,NULL,'¿Cómo debe quedar el auto si es estacionado en subida?','P'),
(36,NULL,'Está prohibido estacionar un vehículo en:','P'),
(37,NULL,'El uso del cinturón de seguridad es obligatorio para:','P'),
(38,NULL,'¿Para quién están destinadas las aceras de la vía pública?','P'),
(39,39,'¿Qué indica esta señalética?','P'),
(40,40,'¿Qué indica esta señalética?','P'),
(41,41,'¿Qué indica esta señalética?','P'),
(42,42,'¿Qué indica esta señalética?','P'),
(43,43,'¿Qué indica esta señalética?','P'),
(44,NULL,'¿En qué casos los vehículos que transiten por cruceros de ferrocarril no podrán cruzar?','P'),
(45,NULL,'Si al momento de la revisión por un agente de tránsito los datos de la tarjeta de circulación no coinciden con los datos del vehículo que conduce, ¿qué procede?','P'),
(46,NULL,'Si en una intersección una calle esta pavimentada y la otra es de terracería ¿cuál de ellas tiene la preferencia?','P'),
(47,NULL,'El paso “uno x uno” para facilitar el tránsito de los vehículos es un acto de:','P'),
(48,NULL,'Es una obligación de los conductores de bicicleta:','P'),
(49,NULL,'Los pasos de cebra marcados en el pavimento señalan el derecho de paso a:','P'),
(50,NULL,'Los escolares gozarán de preferencia para ascenso y descenso de vehículos y acceso o salida de sus centros de estudios','P');
/*!40000 ALTER TABLE `preguntas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `respuestas`
--

DROP TABLE IF EXISTS `respuestas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `respuestas` (
  `id_respuesta` int(11) NOT NULL,
  `id_pregunta` int(11) DEFAULT NULL,
  `opcion` varchar(255) DEFAULT NULL,
  `ok` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id_respuesta`),
  KEY `id_pregunta` (`id_pregunta`),
  CONSTRAINT `respuestas_ibfk_1` FOREIGN KEY (`id_pregunta`) REFERENCES `preguntas` (`id_pregunta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `respuestas`
--

LOCK TABLES `respuestas` WRITE;
/*!40000 ALTER TABLE `respuestas` DISABLE KEYS */;
INSERT INTO `respuestas` VALUES
(1,1,'Encender las luces.',0),
(2,1,'Colocarse el cinturón de seguridad.',1),
(3,1,'Activar la alarma.',0),
(4,2,'a) En el asiento trasero.',1),
(5,2,'b) En el asiento delantero.',0),
(6,2,'c) En la cajuela.',0),
(7,3,'a) Abuso de autoridad.',0),
(8,3,'b) Ninguna infracción.',0),
(9,3,'c) Infracción y delito.',1),
(10,4,'a) Bajar la velocidad.',0),
(11,4,'b) Acelera y pasar primero.',0),
(12,4,'c) Permitirle el paso, colocarse en el extremo de la vialidad y hacer alto total.',1),
(13,5,'a) Si es o transporta persona con discapacidad.',1),
(14,5,'b) Si es el único espacio disponible.',0),
(15,5,'c) Si se estaciona sólo por unos cuantos minutos.',0),
(16,6,'Disminuir velocidad.',0),
(17,6,'No estacionarse.',0),
(18,6,'Circulación en doble sentido.',1),
(19,7,'Legal para no estresarse.',0),
(20,7,'Infracción a las normas de vialidad.',1),
(21,7,'Causa de detención del vehículo.',0),
(22,8,'Intransferibles que identifican al vehículo.',1),
(23,8,'Se requieren para pago de refrendo.',0),
(24,8,'Para obtención de licencia.',0),
(25,9,'El conductor con licencia y tarjeta de circulación.',1),
(26,9,'El agente de tránsito y el conductor.',0),
(27,9,'Únicamente el agente vial y deberá acercarse por el lado del conductor portando casco y gafete de identificación.',0),
(28,10,'Informativas del destino.',0),
(29,10,'Preventivas.',0),
(30,10,'Restrictivas.',1),
(31,11,'Alto total.',0),
(32,11,'Preventiva.',1),
(33,11,'Zona de hospitales.',0),
(34,12,'Desviación.',0),
(35,12,'Vuelta continúa.',0),
(36,12,'Zona escolar.',1),
(37,13,'Verificar niveles, llantas y espejos.',1),
(38,13,'Amortiguadores, radio, calefacción.',0),
(39,13,'Vestiduras, extinguidor y aire acondicionado.',0),
(40,14,'Desde que empiece a oscurecer, de noche, o cuando no haya suficiente visibilidad en el día.',1),
(41,14,'Desde que empieza a circular.',0),
(42,14,'Cuando circule por intersecciones.',0),
(43,15,'Rótulos, carteles u objetos que obstruyan la visibilidad y vidrios polarizados.',1),
(44,15,'Propaganda política que te identifique con algún partido político.',0),
(45,15,'Chip de REPUVE.',0),
(46,16,'Sirenas, faros rojos, torretas, luces blancas o aditamentos exclusivos de unidades destinadas a la seguridad pública.',1),
(47,16,'Cuartos delanteros de luz ámbar y traseros de luz roja.',0),
(48,16,'Claxon cuya potencia no lastime los oídos de los transeúntes y conductores.',0),
(49,17,'Orillarse y usar su unidad para detener el tráfico vehicular.',0),
(50,17,'Si observa que uno de los implicados se aleja a alta velocidad, deberá tomar fotografía con su teléfono celular de las placas.',0),
(51,17,'Seguir su marcha, salvo que las autoridades que estén presentes en el lugar del accidente, soliciten su apoyo.',1),
(52,18,'Proponer que cada conductor se haga cargo de los daños de vehículo y retirarse.',0),
(53,18,'Tratar de llegar a un acuerdo y en caso negativo, acompañar a la autoridad ante el Agente del Ministerio Público y los vehículos serán remitidos al corralón autorizado.',1),
(54,18,'Llamar al seguro y dirigirse a la agencia.',0),
(55,19,'Credencial del INE y placa delantera.',0),
(56,19,'Dos placas, tarjeta de circulación y licencia.',0),
(57,19,'Placa, tarjeta de circulación o licencia de conducir. Solo una de estas tres.',1),
(58,20,'Verde: vía libre para el conductor respetando los límites de velocidad establecidos. Rojo: Alto total. Ámbar: precaución ya que está próximo a cambiar el semáforo en rojo.',1),
(59,20,'Verde en máxima velocidad y rojo bajar la velocidad. La luz amarilla dependerá del horario del día.',0),
(60,20,'Luz verde permitir el paso a los peatones, si no hay quien cruce la calle me puedo pasar. Luz roja alto total y si no hay peatones también me puedo pasar.',0),
(61,21,'Preventivas, restrictivas e informativas.',1),
(62,21,'Escolares, turísticas y comerciales.',0),
(63,21,'Para transporte público y privado.',0),
(64,22,'Sí.',0),
(65,22,'No.',1),
(66,23,'Sí, siempre y cuando el conductor no consuma bebidas alcohólicas.',0),
(67,23,'No, conductor y acompañantes deben abstenerse de consumir bebidas alcohólicas.',1),
(68,23,'Sí, siempre y cuando el consumo no rebase los límites del alcoholímetro.',0),
(69,24,'La factura del vehículo.',0),
(70,24,'La tarjeta de circulación.',1),
(71,24,'El formato RVS07 que se expide en las delegaciones de la SECTE.',0),
(72,25,'Cuando olvide colocarlas en mi vehículo.',0),
(73,25,'Salvo causa justificada que acredite con el documento idóneo.',1),
(74,25,'En ningún caso.',0),
(75,26,'Cuatro metros.',0),
(76,26,'Un metro.',0),
(77,26,'La suficiente para que ingrese un vehículo si busca rebasarme.',1),
(78,27,'Menores de doce años.',1),
(79,27,'Adultos mayores de 65 años.',0),
(80,27,'Ninguno.',0),
(81,28,'Bajar la velocidad.',1),
(82,28,'Mantener la misma velocidad.',0),
(83,28,'Aumentar la velocidad.',0),
(84,29,'40 Kilómetros por hora.',0),
(85,29,'60 Kilómetros por hora.',1),
(86,29,'20 Kilómetros por hora.',0),
(87,30,'20 kilómetros por hora.',1),
(88,30,'30 Kilómetros por hora.',0),
(89,30,'Variable dependiendo las indicaciones del agente de tránsito.',0),
(90,31,'No.',0),
(91,31,'Si.',0),
(92,31,'Sí, salvo que exista señalamiento que indique lo contrario.',1),
(93,32,'La que resulte necesaria.',0),
(94,32,'10 metros.',1),
(95,32,'Una cuarta parte de la longitud de la calle.',0),
(96,33,'20 centímetros.',1),
(97,33,'La que permita la maniobra de estacionamiento.',0),
(98,33,'Una distancia prudente.',0),
(99,34,'Con freno de mano y las llantas en sentido inverso a la acera.',0),
(100,34,'Con freno de mano y las ruedas delanteras dirigidas hacia la acera.',1),
(101,34,'Con freno de mano y las llantas en dirección al sentido de la circulación de la calle.',0),
(102,35,'Con freno de mano y las ruedas delanteras en posición inversa a la acera.',1),
(103,35,'Con freno de mano y las llantas en el mismo sentido de la acera.',0),
(104,35,'Con freno de mano y las llantas en dirección al sentido de la circulación de la calle.',0),
(105,36,'En las aceras, camellones, puentes y en la entrada de vehículos de casas particulares.',1),
(106,36,'En estacionamientos.',0),
(107,36,'En zonas de parquímetros.',0),
(108,37,'El conductor.',0),
(109,37,'Todos los que viajen en el auto.',1),
(110,37,'Conductor y acompañante de asiento delantero.',0),
(111,38,'Peatones.',1),
(112,38,'Vehículos.',0),
(113,38,'Grúas.',0),
(114,39,'Prohibido girar a la izquierda.',0),
(115,39,'Prohibido dar vuelta en “U”.',1),
(116,39,'Obras en proceso de construcción.',0),
(117,40,'Prohibido girar a la izquierda.',1),
(118,40,'Prohibido dar vuelta en “U”.',0),
(119,40,'Glorieta con retorno.',0),
(120,41,'Seguir de frente.',0),
(121,41,'Sin estacionamiento.',0),
(122,41,'Prohibido doblar a la izquierda.',1),
(123,42,'No hay extinguidor.',0),
(124,42,'Sin lugares, pase al siguiente estacionamiento.',0),
(125,42,'Prohibido estacionarse.',1),
(126,43,'No hay extinguidor.',0),
(127,43,'Sin lugares, pase al siguiente estacionamiento.',0),
(128,43,'Prohibido avanzar.',1),
(129,44,'Cuándo esté lloviendo.',0),
(130,44,'Cuando un tren en marcha se encuentre aproximadamente a doscientos metros del cruce o emita una señal audible.',1),
(131,44,'En días inhábiles.',0),
(132,45,'Solicitar la corrección en la Secretaría de Comunicaciones y Transportes.',0),
(133,45,'Entregar la tarjeta al oficial y recibir la infracción.',0),
(134,45,'El vehículo será remitido al corralón autorizado y lo pondrá a disposición de la autoridad competente.',1),
(135,46,'Dependiendo la cantidad de tráfico vehicular.',0),
(136,46,'La pavimentada. ',1),
(137,46,'La de terracería.',0),
(138,47,'Educación.',0),
(139,47,'Es una obligación señalada en el artículo 132 del Reglamento de la Ley de Comunicaciones y Transportes en Materia de Transporte Público y Privado.',1),
(140,47,'De caballerosidad para ceder el paso a las mujeres.',0),
(141,48,'Transitar en el lado opuesto de la circulación',0),
(142,48,'Circular por la extrema derecha de la vía respetando la formación de vehículos en tránsito sin colocarse entre dos de ellos.',1),
(143,48,'Utilizar ambos carriles y circular de forma paralela con los vehículos.',0),
(144,49,'Peatones.',1),
(145,49,'Personas de la tercera edad.',0),
(146,49,'Vehículos particulares.',0),
(147,50,'Cierto.',1),
(148,50,'Falso.',0),
(149,50,'Solo en escuelas de nivel pre escolar y básico.',0);
/*!40000 ALTER TABLE `respuestas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL,
  `rol` enum('admin','estudiante') NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES
(1,'cecilio','admin@admin.com','12345','admin');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'simulacion'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-04-26  0:56:33
