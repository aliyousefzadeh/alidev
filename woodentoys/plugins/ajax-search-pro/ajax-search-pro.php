<?php
/*
Plugin Name: Ajax Search Pro
Plugin URI: https://temifa.ir/product/ajax-search-pro-%d8%a7%d9%81%d8%b2%d9%88%d9%86%d9%87/
Description: قوی ترین افزونه سرج در جهان - ارائه شده توسط تمیفا - برای آموزش افزونه به وبسایت تمیفا مراجعه کنید
Version: 4.16.3
Author: برای دریافت آخرین بروز رسانی از سرور تمیفا کلیک کنید
Author URI: https://temifa.ir/product/ajax-search-pro-%d8%a7%d9%81%d8%b2%d9%88%d9%86%d9%87/
Text Domain: ajax-search-pro
Domain Path: /languages/
*/

/* Prevent direct access */
defined('ABSPATH') or die("You can't access this file directly.");

define('ASP_FILE', __FILE__);
define('ASP_PATH', plugin_dir_path(__FILE__));
define('ASP_CSS_PATH', plugin_dir_path(__FILE__)."/css/");
define('ASP_INCLUDES_PATH', plugin_dir_path(__FILE__)."/includes/");
define('ASP_CLASSES_PATH', plugin_dir_path(__FILE__)."/includes/classes/");
define('ASP_EXTERNALS_PATH', plugin_dir_path(__FILE__)."/includes/externals/");
define('ASP_FUNCTIONS_PATH', plugin_dir_path(__FILE__)."/includes/functions/");
define('ASP_TT_CACHE_PATH', plugin_dir_path(__FILE__)."/includes/cache/");
define('ASP_DIR', 'ajax-search-pro');
define('ASP_PLUGIN_NAME', 'ajax-search-pro/ajax-search-pro.php');
define(
    'ASP_URL',
    strpos(home_url('/'), 'https://') !== false || strpos(plugin_dir_url(__FILE__), 'https://') !== false ?
    str_replace('http://', 'https://', plugin_dir_url(__FILE__)) : plugin_dir_url(__FILE__)
);
define('ASP_URL_NP',  str_replace(array("http://", "https://"), "//", plugin_dir_url(__FILE__)));
define('ASP_CURR_VER', 4988);
define('ASP_CURR_VER_STRING', "4.16.3");
define('ASP_PLUGIN_SLUG', plugin_basename(__FILE__) );
define('ASP_DEBUG', 0);
define('ASP_DEMO', get_option('wd_asp_demo', 0) );
// The one and most important global
global $wd_asp;

require_once(ASP_CLASSES_PATH . "core/core.inc.php");
/**
 *  wd_asp()->_prefix      => correct DB prefix for ASP databases
 *  wd_asp()->tables       => table names
 *  wd_asp()->db           => DB manager
 *  wd_asp()->options      => array of default option arrays
 *  wd_asp()->o            => alias of wd_asp()->options
 *  wd_asp()->instances    => array of search instances and data
 *  wd_asp()->init         => initialization object
 *  wd_asp()->manager      => main manager object
 *  wd_asp()->upload_dir   => the upload directory name
 *  wd_asp()->upload_path  => the upload path (with backslash)
 */
$wd_asp = new WD_ASP_Globals();

if ( !function_exists("wd_asp") ) {
    /**
     * Easy access of the global variable reference
     *
     * @return WD_ASP_Globals
     */
    function wd_asp() {
        global $wd_asp;
        return $wd_asp;
    }
}

// Initialize the plugin
$wd_asp->manager = WD_ASP_Manager::getInstance();
