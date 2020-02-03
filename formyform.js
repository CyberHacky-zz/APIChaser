import { axios } from 'axios';

const API_URL_INPUT = "apiUrlInput";
const METHOD_DROP_DOWN = "methodDropDown";
const API_SUBMIT_BUTTON = "apiSubmitButton";

const apiUrl = document.getElementById(API_URL_INPUT);
const allMethods = document.getElementById(METHOD_DROP_DOWN);
const apiSubmitButton = document.getElementById(API_SUBMIT_BUTTON);

apiSubmitButton.addEventListener('click', () => {
    console.log(apiUrl.value, allMethods.options[allMethods.selectedIndex].text);
});
