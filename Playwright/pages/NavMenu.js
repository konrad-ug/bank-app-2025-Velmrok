class NavMenu {
    constructor(page) {
      this.page = page;
      
    }
  
    async goto() {
      await this.page.goto('https://mfi.ug.edu.pl/');
    }
  
    async clickPracownicy() {
      await this.page.getByRole('link', { name: 'Pracownicy', exact: true }).first().click();
    }
  }
  
  module.exports = { NavMenu };