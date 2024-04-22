<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'woodentoys' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'password' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         's.gKicJu(1hG,Ro3<*O{uu((Fi8MVT&T)QT2CzO<JDv*-0.bCs#tF1|BwSupAq3;' );
define( 'SECURE_AUTH_KEY',  'm`Yf/|$f`QDb-m,DGv!&2?W8U(~ldKLj%aFf9?I9^$C-.]}/$id+?(NCOp6{a0;w' );
define( 'LOGGED_IN_KEY',    '4R`0^W8-:W6Qe9;i)n:s>G#QNMo*l_?bIND]=(Z-jF4+zR^ ]F[(z#(Q^;xTh?#h' );
define( 'NONCE_KEY',        'w[j@%:enTCs2g9Zjw dz:37-sgpadHCfs{%^EyS0{I;{* MHCOkOp*$uTh.R.2g(' );
define( 'AUTH_SALT',        '{VS +3si&bod|dYat0p`&i2EI3g^cl;y-@IjtBKw!QVT(oez3bR.XQTIJr7wh pm' );
define( 'SECURE_AUTH_SALT', '6d2jg}jR)t54wd9QMChLWQfyBz<e,iD)$j@NEp`e(eor0:;s/3Q(YWd)_?>=%BuP' );
define( 'LOGGED_IN_SALT',   '3Qba>{(-}*IFG8*-s%!}hwOh&Wg^;0*xYJ@`:1loX5E*!>l`D}qlQ4LFw0Jyv6h2' );
define( 'NONCE_SALT',       '#P,NFS3uF]`=LMFG;LZ^ atxWe>x(xWAO*=KAYpKKP&WhJjM)]~;Z=AGU 68E }h' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_woodentoys';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
