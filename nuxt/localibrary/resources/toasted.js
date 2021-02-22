/**
 * resources/toasted.js
 *
 * This file defines resources (objects, functions, etc.) that are used
 * in the local implementation of the @nuxt/toast module.
 */

// Actions are added to toasts as objects so here I am defining
// some actions I plan to make frequent use of.
const actions = {
  closeToast: {
    icon: "close-circle-outline",
    onClick: (e, toastObject) => {
      toastObject.goAway(500);
    }
  }
};

export default { actions };
