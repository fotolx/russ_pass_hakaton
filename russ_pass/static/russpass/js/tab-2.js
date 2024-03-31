const tab = document.querySelectorAll(".tab");
const toggleTab = function (element) {
  const tabBtn = element.querySelectorAll(".tab-btn");
  const tabContent = element.querySelectorAll(".tab-content");
  tabBtn[0].classList.add("tab-open");
  tabContent[0].classList.add("tab-open");

  const removeTab = function (element) {
    for (const i of element) {
      i.classList.remove("tab-open");
    }
  };
  const openTab = function (index) {
    removeTab(tabBtn);
    removeTab(tabContent);
    tabBtn[index].classList.add("tab-open");
    tabContent[index].classList.add("tab-open");
  };
  tabBtn.forEach((el, i) => (el.onclick = () => openTab(i)));
};
[...tab].forEach((el) => toggleTab(el));