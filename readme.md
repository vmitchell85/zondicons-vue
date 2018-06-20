# Zondicons Vue Component

This is a basic [Zondicons](http://www.zondicons.com/) [VueJS](https://vuejs.org/) Component.

This was created in part from the ideas in this Twitter thread: [https://twitter.com/paulredmond/status/939226563207249920](https://twitter.com/paulredmond/status/939226563207249920)

## Usage

First you'll need to copy the `zondicon.vue` file into your project and include it in your Vue application. In my Laravel applications I put the following in my `resources/assets/app.js` file.

```js
    Vue.component('z', require('./components/zondicon.vue'));
```

To display an icon just use the component passing the desired icon name and any desired classes.

```html
    <z icon="cheveron-right" class="mx-1 fill-current w-4 h-4"></z>
```


## Generating New Library Content

If you would like to re-generate the library part of the component I've included my crude python script that I used to generate the data from the Zondicons library.