const render_code = () => {
  let html = data_ecom_preview.map((item, index) => {
    return `
      <div class="ec_slide_item swiper-slide" ec_id="${item.id}">
        <div class="ec_slide_inner position-relative">
          <div class="ec_slide_gradient"></div>
          <div class="ec_slide_content">
            <div class="ec_minisize">
              <span></span>
              <span></span>
              <span></span>
            </div>
            <div class="ec_slide_img">
              <div class="hdt-ratio" style="--aspect-ratioapt: 336/355;">
                <!-- Removed the <a> tag to prevent redirect -->
                <picture>
                  <source media="(max-width: 767px)" srcset="./assets/images/ec_demo/mobile/${item.src}">
                  <img loading="lazy" class="lazyloaded" src="./assets/images/ec_demo/${item.src}" data-src="./assets/images/ec_demo/${item.src}" alt="Land Masters demo ${item.id}">
                </picture>
                <div class="ec_pre_btn">
                  <!-- Removed the <a> tag here as well -->
                  <button class="hdt-btn hdt-btn-style1 hdt-btn-hover-icon">Demo</button>
                </div>
              </div>
            </div>
            <div class="title_wrap d-flex justify-content-between align-items-center">
              <span class="title">${item.name}</span>
              <div class="label_user">
                ${item.vip ? `<div class="premium swkx">
                  <svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8" fill="none">
                    <path d="M11.026 1.48218C10.967 1.43184 10.8946 1.3998 10.8177 1.39C10.7408 1.3802 10.6627 1.39307 10.593 1.42701L8.41251 2.4885L6.36659 0.129594C6.32919 0.0864616 6.28296 0.0518703 6.23102 0.0281634C6.17909 0.00445641 6.12267 -0.0078125 6.06558 -0.0078125C6.00849 -0.0078125 5.95206 0.00445641 5.90013 0.0281634C5.8482 0.0518703 5.80196 0.0864616 5.76456 0.129594L3.71864 2.48848L1.5382 1.42699C1.46848 1.39306 1.39037 1.3802 1.31345 1.39C1.23652 1.3998 1.16413 1.43183 1.10515 1.48217C1.04616 1.5325 1.00314 1.59896 0.981367 1.67338C0.959591 1.7478 0.960003 1.82696 0.982552 1.90116L2.49669 6.88188C2.52154 6.96363 2.57201 7.03522 2.64065 7.0861C2.70929 7.13698 2.79247 7.16445 2.87792 7.16444H9.25324C9.33868 7.16445 9.42185 7.13698 9.49049 7.08611C9.55913 7.03523 9.6096 6.96364 9.63444 6.8819L11.1486 1.90118C11.1711 1.82698 11.1716 1.74782 11.1498 1.67339C11.128 1.59897 11.085 1.53251 11.026 1.48218ZM8.95788 6.36753H3.17323L2.01071 2.54337L3.64483 3.33891C3.72372 3.37732 3.81307 3.38861 3.89904 3.37104C3.985 3.35346 4.06276 3.30801 4.12025 3.24173L6.06558 0.99881L8.01093 3.24173C8.06841 3.30801 8.14617 3.35347 8.23213 3.37104C8.31809 3.38861 8.40744 3.37732 8.48633 3.33891L10.1204 2.54337L8.95788 6.36753Z" fill="currentColor"/>
                  </svg>
                  <span>Premium</span>
                </div>` : `<div class="free swkx">
                  <span>Free</span>
                </div>`}
              </div>
            </div>
          </div>
        </div>
      </div>`;
  });

  document.getElementById('render_ecom_preview').innerHTML = html.join("").split(",")
}
// render_code()
