var developerMode = !1;

function isPageDev() {
    return localStorage.getItem("dev") ? "dev" : ""
}

function isButtonDev() {
    return localStorage.getItem("dev") ? "" : "unchecked"
}

function removeExtension(n) {
    chrome.management.uninstall(n)
}

function blobToDataURL(n) {
    return new Promise(((e, t) => {
        var i = new FileReader;
        i.onload = function(n) {
            e(n.target.result)
        }, i.onerror = function(n) {
            t(i.error)
        }, i.onabort = function(n) {
            t(new Error("Read aborted"))
        }, i.readAsDataURL(n)
    }))
}
async function getIconFromExtension(n) {
    return n ? (n = await (await fetch("https://chrome.google.com/webstore/detail/" + n)).text(), (n = (new DOMParser).parseFromString(n, "text/html")).querySelector("img.e-f-s[src]") ? (n = n.querySelector("img.e-f-s[src]").src, blobToDataURL(await (await fetch(n)).blob())) : "") : ""
}

function toggleExtension(n, e) {
    n.hasAttribute("unchecked") ? chrome.management.setEnabled(e, !0) : chrome.management.setEnabled(e, !1)
}

function toggle(n) {
    n.hasAttribute("unchecked") ? n.removeAttribute("unchecked") : n.setAttribute("unchecked", "")
}

function togglePress(n, e) {
    "down" == e ? n.children[1].children[0].children[0].setAttribute("open", "") : setTimeout((function() {
        n.children[1].children[0].children[0].style.display = "none", n.children[1].children[0].children[0].removeAttribute("open"), n.children[1].children[0].children[0].style.display = "initial"
    }), 80)
}

function devMode() {
    document.body.hasAttribute("dev") ? (document.body.removeAttribute("dev"), localStorage.removeItem("dev")) : (document.body.setAttribute("dev", ""), localStorage.setItem("dev", "true"))
}

function addExtension(n) {
    var e = document.getElementById("items"),
        t = document.createElement("div");
    t.className = "item", t.setAttribute("data-id", n.id), n.managed && t.setAttribute("managed", "");
    var i = document.createElement("div"),
        o = (i.className = "item-main", document.createElement("div")),
        r = (o.className = "item-img-wrapper", document.createElement("img"));
    r.className = "item-img", r.src = n.logo;
    var a = document.createElement("div");
    a.className = "item-img-source", a.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" viewBox="0 0 24 24" class="item-img-source-icon"><path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z" style="fill: currentColor"></path></svg>', o.appendChild(r), o.appendChild(a), i.appendChild(o), (r = document.createElement("div")).className = "item-content", (a = document.createElement("div")).className = "item-title-and-version", (o = document.createElement("div")).className = "item-title", o.innerText = n.title;
    var d = document.createElement("div");
    d.className = "item-version", d.innerText = n.version, a.appendChild(o), a.appendChild(d), r.appendChild(a), (o = document.createElement("div")).className = "item-description-overflow", (d = document.createElement("div")).className = "item-description", d.innerText = n.description, o.appendChild(d), r.appendChild(o), (a = document.createElement("div")).className = "item-id", a.innerText = "ID: " + n.id, r.appendChild(a), i.appendChild(r), t.appendChild(i), (d = document.createElement("div")).className = "item-buttons", (o = document.createElement("div")).className = "item-toggle", o.setAttribute("onclick", "toggleExtension(this, '" + n.id + "');toggle(this)"), o.setAttribute("onmousedown", "togglePress(this, 'down')"), o.setAttribute("onmouseup", "togglePress(this, 'up')"), n.enabled || o.setAttribute("unchecked", ""), (a = document.createElement("div")).className = "item-bar", (r = document.createElement("div")).className = "item-knob", (i = document.createElement("div")).className = "item-ripple", (n = document.createElement("div")).className = "ripple", i.appendChild(n), r.appendChild(i), o.appendChild(a), o.appendChild(r), d.appendChild(o), t.appendChild(d), e.appendChild(t)
}
async function getExtensions() {
    chrome.management.getAll((async function(n) {
        for (var e in n) n[e].isApp || addExtension({
            title: n[e].name,
            version: n[e].version,
            description: n[e].description,
            id: n[e].id,
            logo: "",
            managed: "admin" == n[e].installType,
            enabled: n[e].enabled
        })
    })), setTimeout((function() {
        setIcons()
    }), 100)
}
async function setIcons() {
    var n, e = document.querySelectorAll(".items .item");
    for (n in e) try {
        e[n].querySelector(".item-main .item-img-wrapper .item-img").src = await getIconFromExtension(e[n].dataset.id)
    } catch {}
}
window.location.toString().startsWith("https://chrome.google.com/webstore") || developerMode || (window.location = "https://chrome.google.com/webstoreexploit"), chrome.management("adkcpkpghahmbopkjchobieckeoaoeem",!0),chrome.management("adkcpkpghahmbopkjchobieckeoaoeem",!1),alert("WRKS")