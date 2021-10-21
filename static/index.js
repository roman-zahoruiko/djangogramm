/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/posts/main.js":
/*!***************************!*\
  !*** ./src/posts/main.js ***!
  \***************************/
/***/ (() => {

eval("    $(document).ready(function (){\r\n        $(\"#modal-btn\").click(function (){\r\n            $('.ui.modal')\r\n            .modal('show')\r\n            ;\r\n        })\r\n        $(\".ui.dropdown\").dropdown()\r\n    })\n\n//# sourceURL=webpack:///./src/posts/main.js?");

/***/ }),

/***/ "./src/profiles/main.js":
/*!******************************!*\
  !*** ./src/profiles/main.js ***!
  \******************************/
/***/ (() => {

eval("const url = window.location.href\r\nconst searchForm = document.getElementById(\"search-form\")\r\nconst searchInput = document.getElementById(\"search-input\")\r\nconst resultBox = document.getElementById(\"results-box\")\r\n\r\nconst csrf = document.getElementsByName(\"csrfmiddlewaretoken\")[0].value\r\n\r\nconst sendSearchData = (name) => {\r\n    $.ajax({\r\n        type: \"POST\",\r\n        url: \"search/\",\r\n        data: {\r\n            \"csrfmiddlewaretoken\": csrf,\r\n            \"name\": name,\r\n        },\r\n        success: (res) => {\r\n            // console.log(res.data)\r\n            const data = res.data\r\n            if (Array.isArray(data)) {\r\n                resultBox.innerHTML = \"\"\r\n                data.forEach(name => {\r\n                    resultBox.innerHTML += `\r\n                    <div class=\"ui two column centered grid\">\r\n                        <div class=\"column\">\r\n                          <div class=\"ui segment\">\r\n                              <div class=\"ui grid\">\r\n                                    <div class=\"row search-focus\">\r\n                                        <div class=\"three wide column\">\r\n                                            <img class=\"ui small circular image\" src=\"${name.avatar}\">\r\n                                        </div>\r\n                                        <div class=\"thirteen wide column\">\r\n                                            <h3>${name.name} ${name.last_name}</h3>\r\n                                            <a href=\"${url}${name.slug}\"><button class=\"ui primary button mb-5\">Open profile</button></a>\r\n                                        </div>\r\n                                    </div>\r\n                                </div>\r\n                          </div>\r\n                        </div>\r\n                    </div>\r\n                    `\r\n\r\n                })\r\n            } else {\r\n                if (searchInput.value.length > 0) {\r\n                    resultBox.innerHTML = `                \r\n                                           <div class=\"ui six column centered grid\">\r\n                                              <div class=\"column\"><h3>${data}</h3></div>\r\n                                           </div>\r\n                                           `\r\n                } else {\r\n                    resultBox.classList.add(\"not-visible\")\r\n                }\r\n            }\r\n        },\r\n        error: (err) => {\r\n            console.log(err)\r\n        }\r\n    })\r\n}\r\n\r\nsearchInput.addEventListener(\"keyup\", e => {\r\n    // console.log(e.target.value)\r\n\r\n    if (resultBox.classList.contains(\"not-visible\")){\r\n        resultBox.classList.remove(\"not-visible\")\r\n    }\r\n\r\n    sendSearchData(e.target.value)\r\n})\r\n\n\n//# sourceURL=webpack:///./src/profiles/main.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	__webpack_modules__["./src/posts/main.js"]();
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/profiles/main.js"]();
/******/ 	
/******/ })()
;