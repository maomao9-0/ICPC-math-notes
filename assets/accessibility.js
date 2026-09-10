// Quarto's collapsible callout headers are divs; give keyboard users the same
// activation behavior as pointer users. Bootstrap still owns collapse state.
document.addEventListener('DOMContentLoaded', () => {
  for (const header of document.querySelectorAll('.callout [data-bs-toggle="collapse"]')) {
    if (header.matches('button, a[href], input')) continue;
    header.setAttribute('role', 'button');
    header.tabIndex = 0;
    header.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        header.click();
      }
    });
  }
});
