# anarmedia.mn
<section id="order" style="padding:60px 20px; background:#fff;">
    <div style="max-width:600px; margin:auto;">
        <h2 style="text-align:center; margin-bottom:10px;">
            Бараа захиалга
        </h2>

        <p style="text-align:center; margin-bottom:30px;">
            Та захиалах бараагаа сонгоод мэдээллээ оруулна уу.
        </p>

        <form id="orderForm">

            <label>Бараа сонгох</label>
            <select id="product" required
                style="width:100%; padding:14px; margin:8px 0 18px;">
                <option value="">-- Бараа сонгох --</option>
                <option value="Бараа 1">Бараа 1</option>
                <option value="Бараа 2">Бараа 2</option>
                <option value="Бараа 3">Бараа 3</option>
            </select>

            <label>Тоо ширхэг</label>
            <input type="number" id="quantity" min="1" value="1" required
                style="width:100%; padding:14px; margin:8px 0 18px;">

            <label>Нэр</label>
            <input type="text" id="name" placeholder="Таны нэр" required
                style="width:100%; padding:14px; margin:8px 0 18px;">

            <label>Утасны дугаар</label>
            <input type="tel" id="phone" placeholder="99112233" required
                style="width:100%; padding:14px; margin:8px 0 18px;">

            <label>Хаяг</label>
            <textarea id="address" placeholder="Хүргэлт хийх хаяг" required
                style="width:100%; padding:14px; margin:8px 0 18px; min-height:100px;"></textarea>

            <label>Нэмэлт тайлбар</label>
            <textarea id="note" placeholder="Хэрэв нэмэлт хүсэлт байвал бичнэ үү."
                style="width:100%; padding:14px; margin:8px 0 20px; min-height:80px;"></textarea>

            <button type="submit"
                style="width:100%; padding:16px; border:none; border-radius:8px; background:#dca448; color:white; font-size:18px; cursor:pointer;">
                🛒 Захиалга илгээх
            </button>

        </form>
    </div>
</section>
