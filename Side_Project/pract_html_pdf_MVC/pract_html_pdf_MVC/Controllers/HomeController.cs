using Microsoft.AspNetCore.Mvc;
using pract_html_pdf_MVC.Models;
using System.Diagnostics;

using SelectPdf;

namespace pract_html_pdf_MVC.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        public IActionResult Index()
        {
            ViewData["test"] = "假裝打資料進入頁面";
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

        public FileResult ExportPdf(string htmlData)
        {
            HtmlToPdf objHtml = new HtmlToPdf();
            PdfDocument objDoc = objHtml.ConvertHtmlString(htmlData);
            byte[] pdf = objDoc.Save();
            objDoc.Close();
            return File(pdf, "application/pdf", "Test.pdf");

        }

    }
}