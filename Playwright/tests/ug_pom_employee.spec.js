const { test } = require('@playwright/test');
const { NavMenu } = require('../pages/NavMenu');
const { EmployeeSearchPage } = require('../pages/EmployeeSearchPage');

test.describe('Testy Pracowników UG', () => {

  test('Konrad Soltys', async ({ page }) => {
    const nav = new NavMenu(page);
    const searchPage = new EmployeeSearchPage(page);
    await nav.goto();
    await nav.clickPracownicy()
    await searchPage.clickSkladOsobowy();
    await searchPage.searchForEmployee('Sołtys');
    await searchPage.openEmployeeProfile('mgr Konrad Sołtys');
    await searchPage.expectRoomNumber('Nr pokoju: 4.19');
  });

  test('Anna Baran', async ({ page }) => {
    const nav = new NavMenu(page);
    const searchPage = new EmployeeSearchPage(page);
    await nav.goto();
    await nav.clickPracownicy();
    await searchPage.clickSkladOsobowy();
    await searchPage.searchForEmployee('Baran');
    await searchPage.openEmployeeProfile('mgr Anna Baran');
    await searchPage.expectInstitute('Instytut Fizyki Doświadczalnej');
  });

});