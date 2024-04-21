<?php
if ( ! defined( 'ABSPATH' ) ) {
	exit; // Exit if accessed directly.
}

/**
 * CWLP Social Funtion
 *
 * CWLP Social Funtion is responsible for work plugin social bar options
 *
 * @since 2.0
 */

function cwlp_socials() {
    $direction = is_rtl() ? '-rtl' : '';
    $cwinsta = get_option( 'cwlp-instagram' );
    $cwteleg = get_option( 'cwlp-telegram' );
    $cwpinter = get_option( 'cwlp-pinterest' );
    $cwwhats = get_option( 'cwlp-whatsapp' );
    $cwfaceboo = get_option( 'cwlp-facebook' );
    $cwtwitt = get_option( 'cwlp-twitter' );
    $cwlinked = get_option( 'cwlp-linkedin' );
    $cwdmode = get_option( 'cwlp-dmode' );
    
    if ( empty( $cwteleg ) && empty( $cwinsta ) && empty( $cwpinter ) && empty( $cwwhats ) && empty( $cwfaceboo ) && empty( $cwtwitt ) && empty( $cwlinked ) ) {
        wp_dequeue_style( 'social-bar' );
        wp_deregister_script( 'social-bar' );
    } else {
        add_action( 'login_footer', 'cwlp_social_foot' );
        wp_enqueue_script( 'jquery' );
        wp_enqueue_style( 'font-awesome', CWLP_LOGIN_ASSETS . 'css/awesome/brands.css', '', '6.0' );
        wp_enqueue_style( 'social-bar', CWLP_LOGIN_ASSETS . 'css/cwlp-socialer' . $direction . '.css', array( 'font-awesome' ), '2.0' );
		?>
		<style>
		<?php
		if ( $cwdmode === '0' ) {
			echo '.cwlp-icon-bar a {display: block;}';
		} else {
			echo '.cwlp-icon-bar a {display: inline-block;}';
		}
		?>
		</style>
		<?php
    }
}

function cwlp_social_foot() {
    $cwinsta = get_option( 'cwlp-instagram' );
    $cwteleg = get_option( 'cwlp-telegram' );
    $cwpinter = get_option( 'cwlp-pinterest' );
    $cwwhats = get_option( 'cwlp-whatsapp' );
    $cwfaceboo = get_option( 'cwlp-facebook' );
    $cwtwitt = get_option( 'cwlp-twitter' );
    $cwlinked = get_option( 'cwlp-linkedin' );
    
    ob_start();
    ?>
    <div class="cwlp-icon-bar" id="cwlp-social-n">
        <i class="dashicons dashicons-no close-bu" id="masoudnkh"></i>
        <div class="cwlpsociali">
            <?php if ( ! empty( $cwinsta ) ) : ?>
                <a href="https://www.instagram.com/<?php echo $cwinsta; ?>" class="instagram" target="_blank"><i class="fa fa-instagram"></i></a>
            <?php endif; ?>
            <?php if ( ! empty( $cwteleg ) ) : ?>
                <a href="https://t.me/<?php echo $cwteleg; ?>" class="telegram" target="_blank"><i class="fa fa-telegram"></i></a>
            <?php endif; ?>
            <?php if ( ! empty( $cwpinter ) ) : ?>
                <a href="https://www.pinterest.com/<?php echo $cwpinter; ?>" class="pinterest" target="_blank"><i class="fa fa-pinterest"></i></a>
            <?php endif; ?>
            <?php if ( ! empty( $cwwhats ) ) : ?>
                <a href="https://wa.me/<?php echo $cwwhats; ?>" class="whatsapp" target="_blank"><i class="fa fa-whatsapp"></i></a>
            <?php endif; ?>
            <?php if ( ! empty( $cwfaceboo ) ) : ?>
                <a href="https://www.facebook.com/<?php echo $cwfaceboo; ?>" class="facebook" target="_blank"><i class="fa fa-facebook"></i></a>
            <?php endif; ?>
            <?php if ( ! empty( $cwtwitt ) ) : ?>
                <a href="https://twitter.com/<?php echo $cwtwitt; ?>" class="twitter" target="_blank"><i class="fa fa-twitter"></i></a>
            <?php endif; ?>
            <?php if ( ! empty( $cwlinked ) ) : ?>
                <a href="https://www.linkedin.com/in/<?php echo $cwlinked; ?>" class="linkedin" target="_blank"><i class="fa fa-linkedin"></i></a>
            <?php endif; ?>
        </div>
    </div>
    <?php
    
    $output = ob_get_clean();
    
    echo $output;
    
    if ( empty( $cwteleg ) && empty( $cwinsta ) && empty( $cwpinter ) && empty( $cwwhats ) && empty( $cwfaceboo ) && empty( $cwtwitt ) && empty( $cwlinked ) ) {
        return;
    }
    
    ?>
    <script>
        jQuery(function($) {
            $(".dashicons").click(function() {
                $(this).toggleClass("dashicons-no dashicons-plus adoni");
            });
            $(".dashicons").click(function() {
                $(".cwlpsociali").toggle("slow", function() {});
            });
        });
    </script>
    <?php
}

add_action( 'login_enqueue_scripts', 'cwlp_socials' );
