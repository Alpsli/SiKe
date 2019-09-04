import 'whatwg-fetch';
import {Message, Notification} from 'element-ui';

/**
 * 请求一个URL，返回Promise对象，包含response body，也有可能抛出异常
 *
 * @param  {string} url       The URL we want to request
 * @param  {object} [options] The options we want to pass to "fetch"
 * @return {object}           An object containing either "data" or "err"
 */
export default function request(url, options) {
    let _response = {}; //在error中保留response对象，以保留完整的response信息

    /**
     * 注意:
     * 通过https://vpn.iqiyi.com访问本系统时，由于vpn做了特殊的转发，url形如https://vpn.iqiyi.com/,DanaInfo=bi.qiyi.domain,SSO=U+#/，
     * 此时url如果是"/api/common/init"这种相对路径，最终发出的会变成错误的值，例如https://vpn.iqiyi.com/api/common/init?
     * 所以需要手动重写url的值
     */
    /* if (url.indexOf('http') === -1) {
         if (window.location.pathname.lastIndexOf('/') + 1 === window.location.pathname.length) {
             if (url.indexOf('/') === 0) {
                 url = url.substr(1);
             }
         }
         url = window.location.protocol + '//' + window.location.host + window.location.pathname + url;
     }*/

    return fetch(url, options)
        .then(response => {
            //将body转换为json对象
            _response = response;
            if ((_response.status >= 200 && _response.status < 300) || _response.status == 422
	            || _response.status == 403 || _response.status == 400) {
                return response.json();
            } else {
                return {};
            }
        }).then(json => {
            //对非正常返回抛出错误
            if (_response.status >= 200 && _response.status < 300) {
                return json;
            } else {
                const error = new Error(_response.statusText);
                error.response = _response;
                error.errors = json.errors;
                throw error;
            }
        })
}

/**
 * 快捷get方法
 * 在request的基础上封装
 * @param url
 * @returns {Object}
 */
export function get(url) {
    return request(url, {
        headers: {
            'Content-Type': 'application/json',
            'X-Request-With': 'XMLHttpRequest'
        },
        credentials: 'same-origin'
    });
}

/**
 * 快捷get方法
 * 在request的基础上封装
 * @param url
 * @param payload
 * @returns {Object}
 */
export function post(url, payload) {
    return request(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Request-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(payload),
        credentials: 'same-origin'
    });
}

/**
 * 快捷put方法，RESTful规范要求url以资源ID结尾
 * 在request的基础上封装
 * @param url
 * @param payload
 * @returns {Object}
 */
export function put(url, payload) {
    return request(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-Request-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(payload),
        credentials: 'same-origin'
    });
}

/**
 * 快捷delete方法，RESTful规范要求url以资源ID结尾
 * 在request的基础上封装
 * @param url
 * @returns {Object}
 */
export function del(url, payload) {
    return request(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-Request-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(payload),
        credentials: 'same-origin'
    });
}

/**
 * 根据错误码显示不同的错误提示
 * @param err
 * @param duration
 */
export function handleErr(err, duration = 5000) {
    if (err.response) {
        //request抛出的异常
        switch (err.response.status) {
           /* case 401:
                for (let item of err.errors) {
                    Message({
                        title: item.code,
                        message: item.message ? item.message : '未知错误',
                        type: 'error',
                        duration
                    });
                }
                break;*/
            case 401:
	            Message({
	                message: "您还没有登录，5秒后将跳往登录页",
	                type: 'error',
	                duration,
	                onClose() {
	                    window.location.reload();
	                }
	            });
            break;
	        case 404:
		        Message({
			        message: "接口/页面不存在",
			        type: 'error'
		        });
		        break;
            case 403:
                Message({
                    message: "您没有访问此接口/页面的权限",
                    type: 'error'
                });
                // break;
            case 400:
            case 422:
                for (let item of err.errors) {
                    Notification({
                        title: item.code,
                        message: item.message ? item.message : '未知错误',
                        type: 'error',
                        duration
                    });
                }
                break;
            default:
                Message({
                    message: "错误 " + err.response.status + ": " + err.response.statusText,
                    type: 'error',
                    duration
                });
                break;
        }

    } else {
        console.error(err);
    }
}
