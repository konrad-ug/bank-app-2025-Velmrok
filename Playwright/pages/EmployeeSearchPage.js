const { expect } = require('@playwright/test');

class EmployeeSearchPage {
  constructor(page) {
    this.page = page;
    this.skladOsobowyLink = page.getByRole('link', { name: 'Skład osobowy' }).nth(1);
    this.surnameInput = page.getByLabel('Nazwisko');
    this.searchButton = page.getByRole('button', { name: 'Szukaj' }).nth(1);
  }

  async clickSkladOsobowy() {
   
    await this.skladOsobowyLink.click();
  }

  async searchForEmployee(surname) {
    await this.surnameInput.fill(surname);
    await this.searchButton.click();
  }

  async openEmployeeProfile(fullName) {
    await this.page.getByRole('link', { name: fullName }).first().click();
  }

  async expectRoomNumber(room) {
    await expect(this.page.getByText(room)).toBeVisible();
  }
  
  async expectInstitute(instituteName) {
      await expect(this.page.getByText(instituteName)).toBeVisible();
  }
}

module.exports = { EmployeeSearchPage };