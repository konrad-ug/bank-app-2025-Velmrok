import { test, expect } from '@playwright/test';

test('Check Konrad Soltys room number', async ({ page }) => {
  await page.goto('https://mfi.ug.edu.pl/');
  await page.getByRole('link', { name: 'Pracownicy', exact: true }).first().click();
  await page.getByRole('link', { name: 'Skład osobowy' }).nth(1).click();
  await page.getByLabel('Nazwisko').fill('Sołtys');
  await page.getByRole('button', { name: 'Szukaj' }).nth(1).click();

  const link = page.getByRole('link', { name: 'mgr Konrad Sołtys' });
  await expect(link).toBeVisible();
  await link.click();
  await expect(page.getByText('Nr pokoju: 4.19')).toBeVisible();
});